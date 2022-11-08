'''
    This module displays a creates a graph to be displayed within a notebook. It
    also creates the control buttons and handles the callbacks. Provision is
    also made for non-standard buttons and their associated callbacks.

    The data for a graph is provided by a CSV file, which is provided in the
    constructor. The constructor also accepts the begin and end dates to display.
    If these dates are outside of the actual data, then bad things happen.
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
from mplfinance.original_flavor import candlestick_ohlc

import datetime
import tkinter as tk

class Chart(tk.Frame):
    '''
    Create a chart to display within a notebook frame.
    '''

    def __init__(self, owner, fname, start_date, end_date, **kw):

        super().__init__(owner, **kw)
        self.owner = owner
        self.fname = fname
        self. start_date = start_date
        self.end_date = end_date

        # button constants to avoid scattering them in the code
        self.btn_width = 10
        self.btn_xpad = 5
        self.btn_ypad = 5
        # current row to set the button into
        self.btn_row = 0
        # set up the frame
        self.btn_frame = tk.Frame(self)
        self.btn_frame.grid(row=0, column=0, sticky='se')

        # set up the content frame
        self.ctl_frame = tk.LabelFrame(self)
        self.ctl_frame.grid(row=0, column=1, sticky='nw')

        self._add_button("btn1", self._btn1_cb)
        self._add_button("btn2", self._btn1_cb)
        self._add_button("btn3", self._btn1_cb)

        self.grid()

    def _add_button(self, name, callback, **kw):
        widget = tk.Button(self.btn_frame, text=name, width=self.btn_width, command=callback, **kw)
        widget.grid(row=self.btn_row, column=0, padx=self.btn_xpad, sticky='nw')
        self.btn_row += 1
        return widget

    def _btn1_cb(self):
        print("btn callback")
