
import tkinter as tk
from configuration import Config

#just used to display messages on screen
from tkinter import messagebox

class MainMenu(object):

    def __init__(self, master):
        # build the menu here
        #print("building the main menu")
        self.master = master
        self.config = Config.get_config()

        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self._file_new)
        filemenu.add_command(label="Open", command=self._file_open)
        filemenu.add_separator()
        filemenu.add_command(label="Backup", command=self._file_backup)
        filemenu.add_command(label="Restore", command=self._file_restore)
        filemenu.add_command(label="Clear", command=self._file_clear)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._confirm_exit)
        menubar.add_cascade(label="File", menu=filemenu)

        symbolmenu = tk.Menu(menubar, tearoff=0)
        symbolmenu.add_command(label="Add", command=self._symbol_add)
        symbolmenu.add_command(label="Delete", command=self._symbol_delete)
        symbolmenu.add_command(label="Review", command=self._symbol_review)
        symbolmenu.add_command(label="Setup", command=self._symbol_setup)
        menubar.add_cascade(label="Symbol", menu=symbolmenu)

        rulesmenu = tk.Menu(menubar,tearoff=0)
        rulesmenu.add_command(label="Symbol", command=self._rules_symbol)
        rulesmenu.add_command(label="Add", command=self._rules_add)
        rulesmenu.add_command(label="Delete", command=self._rules_delete)
        rulesmenu.add_command(label="Reset", command=self._rules_reset)
        rulesmenu.add_command(label="Create", command=self._rules_create)
        menubar.add_cascade(label="Rules", menu=rulesmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self._help_about)
        helpmenu.add_command(label="Help", command=self._help_help)
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    
    def _file_new(self):
        messagebox.showinfo("showinfo","you clicked file new")

    def _file_open(self):
        messagebox.showinfo("showinfo","you clicked file open")

    def _file_backup(self):
        messagebox.showinfo("showinfo","you clicked file backup")

    def _file_restore(self):
        messagebox.showinfo("showinfo","you clicked file restore")

    def _file_clear(self):
        messagebox.showinfo("showinfo","you clicked file clear")

    def _symbol_add(self):
        messagebox.showinfo("showinfo","you clicked symbol add")

    def _symbol_delete(self):
        messagebox.showinfo("showinfo","you clicked symbol delete")

    def _symbol_review(self):
        messagebox.showinfo("showinfo","you clicked symbol review")

    def _symbol_setup(self):
        messagebox.showinfo("showinfo","you clicked symbol setup")

    def _rules_symbol(self):
        messagebox.showinfo("showinfo","you clicked rules symbol")

    def _rules_add(self):
        messagebox.showinfo("showinfo","you clicked rules add")

    def _rules_delete(self):
        messagebox.showinfo("showinfo","you clicked rules delete")

    def _rules_reset(self):
        messagebox.showinfo("showinfo","you clicked rules reset")

    def _rules_create(self):
        messagebox.showinfo("showinfo","you clicked rules create")

    def _help_about(self):
        messagebox.showinfo("About Stocks","""
        This is a simple stock security tracker. I am working on it to help me understand the analysis associated with trading stocks, since I have no training and no clue how such analysis actually works. This is not intended to be guidance for trading stocks, or anything else, and will almost certainly lead to wrong choices if someone tries to use it for some purpose or other. This project could be useful for learning python and related things.

This application will be a simple stock tracker that is able to do past analysis on the history of specific stocks. Several types of analysis is planned such as:

Relative Strength Indicator (RSI)
Fibonacci
Bollinger
Breath Thrust Indicator (BTI)
SMA and EMA and others
Other indicator generators.
        """)

    def _help_help(self):
        messagebox.showinfo("showinfo","you clicked help help")
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
