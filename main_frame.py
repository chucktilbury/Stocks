
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
        self.win_height = 700
        self.win_width = 1200
        master.menu_bar = MainMenu(master)
        master.geometry("{w}x{h}".format(w=self.win_width, h=self.win_height))
        self.init_ui()

    def init_ui(self):
        # Add the other use interface stuff here.
        self.notebook = Notebook(self.master, ["Tab1", "Tab2", "Tab3"])
        self.notebook.show_tab(0)
        Chart(self.notebook, "MSFT", "test.csv", "2021-01-04", "2021-02-26",
                panel_height=self.win_height, panel_width=self.win_width)

    def run(self):
        self.master.mainloop()
