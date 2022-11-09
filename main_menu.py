
import tkinter as tk

#just used to diaplay messages on screen
from tkinter import messagebox

class MainMenu(object):

    def __init__(self, master):
        # build the menu here
        #print("building the main menu")
        self.master = master

        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self._displayMsg)
        filemenu.add_command(label="Open", command=self._displayMsg)
        filemenu.add_separator()
        filemenu.add_command(label="Backup", command=self._displayMsg)
        filemenu.add_command(label="Restore", command=self._displayMsg)
        filemenu.add_command(label="Clear", command=self._displayMsg)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._confirm_exit)
        menubar.add_cascade(label="File", menu=filemenu)

        symbolmenu = tk.Menu(menubar, tearoff=0)
        symbolmenu.add_command(label="Add", command=self._displayMsg)
        symbolmenu.add_command(label="Delete", command=self._displayMsg)
        symbolmenu.add_command(label="Review", command=self._displayMsg)
        symbolmenu.add_command(label="Setup", command=self._displayMsg)
        menubar.add_cascade(label="Symbol", menu=symbolmenu)

        rulesmenu = tk.Menu(menubar,tearoff=0)
        rulesmenu.add_command(label="Symbol", command=self._displayMsg)
        rulesmenu.add_command(label="Add", command=self._displayMsg)
        rulesmenu.add_command(label="Delete", command=self._displayMsg)
        rulesmenu.add_command(label="Reset", command=self._displayMsg)
        rulesmenu.add_command(label="Create", command=self._displayMsg)
        menubar.add_cascade(label="Rules", menu=rulesmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self._displayMsg)
        helpmenu.add_command(label="Help", command=self._displayMsg)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)
        self.master.protocol('WM_DELETE_WINDOW', self._confirm_exit)


    def _private_callback_example(self):
        print("something informative")

    def _do_exit(self):
        self.master.destroy()
    
    #Pop up a message on the screen
    def _displayMsg(self):
        messagebox.showinfo("showinfo","you clicked a menu")

    def _confirm_exit(self):
        if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
            self._do_exit()