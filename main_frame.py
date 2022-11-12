
import tkinter as tk
from main_menu import MainMenu
from notebook import Notebook
from chart import Chart
from configuration import Config
from symbols import Symbol

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
        self.config = Config.get_config()
        self.init_ui()

    def init_ui(self):
        # Add the other use interface stuff here.
        self.notebook = Notebook(self.master)

        symb = Symbol('CRHC')
        self.config.add_symbol(symb.name(), symb)
        chart = Chart(self.notebook,
                        panel_height=self.win_height, panel_width=self.win_width)
        chart.create_chart(symb)
        self.notebook.add_tab(symb.name(), chart)

        symb = Symbol('DFIC')
        chart = Chart(self.notebook,
                        panel_height=self.win_height, panel_width=self.win_width)
        chart.create_chart(symb)
        self.notebook.add_tab(symb.name(), chart)

        symb = Symbol('MSFT')
        chart = Chart(self.notebook,
                        panel_height=self.win_height, panel_width=self.win_width)
        chart.create_chart(symb)
        self.notebook.add_tab(symb.name(), chart)

    def run(self):
        self.master.mainloop()
