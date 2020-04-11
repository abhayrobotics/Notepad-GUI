# Notepad

# TODO
# adding bullets
# auto date
# print statement
# adding wordwrap
# convert into ide


from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo, askyesnocancel, showwarning
import os


def newfile():
    global file
    print("1", textarea.get(1.0, END))

    q = askyesnocancel("File not Saved", "Do you want to save the file")
    print(q)
    if q == True:
        savefile()
    elif q == False:
        showwarning("Not Saved", "File not Saved !")
        file = None
        root.title("Untitled - Notepad by Abhay")
        textarea.delete(1.0, END)


def openfile():
    global file
    # creating a dialog box for browsing
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                          ("Text Document", "*.txt")])
    if file == "":
        # if no file is chosen do nothing
        file = None
    else:
        # if a file is chosen from path, use the base name to show on title
        # delete the existing text file and read the open file to insert
        root.title(os.path.basename(file) + " - Notepad by Abhay")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())


def savefile():
    global file
    if file == None:
        # if file is not saved
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt"
                                            , filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])
        if file == "":
            # if nothing in file do nothing
            file = None
        else:
            # Save as a new File
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad by Abhay")
            print("File saved")

    else:
        # if file is already saved and new changes are done just save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def printfile():
    pass


def exitapp():
    root.destroy()


def cut():
    textarea.event_generate("<<Cut>>")


def copy():
    textarea.event_generate("<<Copy>>")


def paste():
    textarea.event_generate("<<Paste>>")


def font1():
    global font_style, font_size, font_width
    print("active", fontcheck.get())

    if fontcheck.get():
        frame10.grid(row=0, column=0)

        Label(frame1, text="Font Style").grid(row=0, column=0)
        Entry(frame1, textvariable=font_style, ).grid(row=0, column=1)

        Label(frame1, text="Font Size").grid(row=0, column=2)
        Entry(frame1, textvariable=font_size).grid(row=0, column=3)

        Label(frame1, text="Font Width").grid(row=0, column=4)
        Entry(frame1, textvariable=font_width).grid(row=0, column=5)

        Button(frame1, text="Apply! ", fg="green", command=applyfont).grid(row=0, column=6)

    else:
        # it unchecked it removes the style bar frame with storing the info
        frame10.grid_remove()


def applyfont():
    print(font_width.get(), font_size.get(), font_style.get())
    # for changing any setting during run Time we use config
    textarea.config(font=f"{font_style.get()} {font_size.get()} {font_width.get()}")


def help():
    showinfo("About Notepad", "Created by: Abhay Kumar \n")


if __name__ == '__main__':
    root = Tk()
    root.geometry("700x500")
    root.title("Untitled - Notepad by Abhay")

    file = None

    # Font style bar
    fontcheck = BooleanVar()

    # grid_rowconfigure  ,make the size of window responsive to the change of window size
    # (index of row/column,weight=1  ,minsize=x)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    frame10 = Frame(root, bg="green")
    # it will contain frame 0 which contain-font style tab
    frame10.grid(row=0, column=0, sticky=W)

    frame20 = Frame(root, bg="red")
    # it will contain the text area frame
    frame20.grid(row=1, column=0, sticky=NSEW)

    frame1 = Frame(frame10, borderwidth=1, relief=SUNKEN, )
    # it will contain the  font style tab
    frame1.pack(fill=X, anchor=N, side=TOP)

    textframe = Frame(frame20)

    # Adding Scroll bar
    scrollbar = Scrollbar(textframe)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Adding text

    font_style = StringVar()
    font_size = IntVar()
    font_width = StringVar()
    font_style.set("lucida")
    font_size.set(12)
    font_width.set("bold")

    textarea = Text(textframe, padx=5, pady=5, font=f"{font_style.get()} {font_size.get()} {font_width.get()} ",
                    yscrollcommand=scrollbar.set)
    textarea.pack(expand=True, fill=BOTH)  # expand the textarea to size of GUI window
    textframe.pack(expand=True, fill=BOTH)
    scrollbar.config(command=textarea.yview)

    menybar2 = Menu(root)
    # File menu
    filemenu = Menu(menybar2, tearoff=0)
    filemenu.add_command(label="New", command=newfile)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_command(label="Print", command=printfile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exitapp)

    menybar2.add_cascade(label="File", menu=filemenu)

    # Edit Menu
    editmenu = Menu(menybar2, tearoff=0)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)

    menybar2.add_cascade(label="Edit", menu=editmenu)

    # Format Menu

    formatmenu1 = Menu(menybar2, tearoff=0)
    formatmenu1.add_checkbutton(label="Show Style bar", onvalue=1, offvalue=0, variable=fontcheck, command=font1)
    # formatmenu1.add_command(label="Font", command=font1)
    menybar2.add_cascade(label="Format", menu=formatmenu1)

    # Help
    helpmenu = Menu(menybar2, tearoff=0)
    helpmenu.add_command(label="About", command=help)
    menybar2.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menybar2)

    root.mainloop()
