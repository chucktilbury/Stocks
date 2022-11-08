
import tkinter as tk
from main_menu import MainMenu
from notebook import Notebook
from chart import Chart

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
        self.notebook = Notebook(self.master, ["Tab1", "Tab2", "Tab3"])
        self.notebook.show_tab(0)
        Chart(self.notebook, "test.csv", "2021-01-04", "2021-02-26")

    def run(self):
        self.master.mainloop()
