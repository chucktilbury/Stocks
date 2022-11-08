
import tkinter as tk

class MainMenu(object):

    def __init__(self, master):
        # build the menu here
        print("building the main menu")

    def _private_callback_example(self):
        print("something informative")

    def _do_exit(self):
        self.master.destroy()
