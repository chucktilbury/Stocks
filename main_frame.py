
import tkinter as tk
from main_menu import MainMenu
from notebook import Notebook
from chart import Chart
from configuration import Config

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
        self.config = Config.get_config()

    def init_ui(self):
        # Add the other use interface stuff here.
        self.notebook = Notebook(self.master)

        chart = Chart(self.notebook,
                        panel_height=self.win_height, panel_width=self.win_width)
        self.notebook.add_tab('CRHC', chart)
        chart.create_chart('CRHC-max.csv', 'CRHC')

        chart = Chart(self.notebook,
                        panel_height=self.win_height, panel_width=self.win_width)
        self.notebook.add_tab('DFIC', chart)
        chart.create_chart('DFIC-max.csv', 'DFIC')

        chart = Chart(self.notebook,
                        panel_height=self.win_height, panel_width=self.win_width)
        self.notebook.add_tab('MSFT', chart)
        chart.create_chart('MSFT-max.csv', 'MSFT')
        self.notebook.show_tab(0)

    def run(self):
        self.master.mainloop()
