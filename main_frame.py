
import tkinter as tk
from main_menu import MainMenu

class MainFrame(object):

    def __init__(self, name):

        self.name = name

        master = tk.Tk()
        master.wm_title(name)
        self.master = master

        master.menu_bar = MainMenu(master)
        master.geometry('950x700')
        self.init_ui()

    def init_ui(self):
        # Add the other use interface stuff here.
        pass

    def run(self):
        self.master.mainloop()
