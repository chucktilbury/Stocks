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

    def __init__(self, owner, name, fname, start_date, end_date, **kw):

        if 'panel_width' in kw:
            self.panel_width = kw['panel_width']
            del kw['panel_width']
        else:
            self.panel_width = 1024

        if 'panel_height' in kw:
            self.panel_height = kw['panel_height']
            del kw['panel_height']
        else:
            self.panel_height = 720

        super().__init__(owner, **kw)
        self.owner = owner
        self.fname = fname
        self. start_date = start_date
        self.end_date = end_date

        self.total_height = self.panel_height - 70
        self.info_frame_width = 250
        self.btn_frame_width = 15
        self.ctl_frame_width = \
            (self.panel_width - \
                (self.info_frame_width + self.btn_frame_width))

        # button constants to avoid scattering them in the code
        self.btn_width = 10
        self.btn_xpad = 5
        self.btn_ypad = 5
        # current row to set the button into
        self.btn_row = 0
        # set up the frame
        self.btn_frame = tk.Frame(self)
        self.btn_frame.config(width=self.btn_frame_width)
        self.btn_frame.config(height=self.total_height)
        self.btn_frame.grid(row=0, column=0, sticky='se')

        self._add_button("Date Right", self._date_right_btn_cb)
        self._add_button("Date Left", self._date_left_btn_cb)
        self._add_button("Setup", self._setup_btn_cb)

        # set up the content frame
        self.ctl_frame = tk.LabelFrame(self, text=name)
        self.ctl_frame.config(width=self.ctl_frame_width)
        self.ctl_frame.config(height=self.total_height+17)
        self.ctl_frame.grid(row=0, column=1, sticky='nw')

        self.info_frame = tk.LabelFrame(self, text='Info')
        self.info_frame.config(width=self.info_frame_width)
        self.info_frame.config(height=self.total_height)
        self.info_frame.grid(row=0, column=2, sticky='nw', padx=7)
        self.info_data_frame = tk.Frame(self.info_frame)
        self.info_data_frame.config(height=self.total_height-35)
        self.info_data_frame.grid(column=0, row=0)
        btn = tk.Button(self.info_frame, text="Refresh", width=self.btn_width, command=self._refresh_btn_cb)
        btn.grid(column=0, row=1)


        self.grid() # display the frame

    def _add_button(self, name, callback, **kw):
        widget = tk.Button(self.btn_frame, text=name, width=self.btn_width, command=callback, **kw)
        widget.grid(row=self.btn_row, column=0, padx=self.btn_xpad, sticky='nw')
        self.btn_row += 1
        return widget

    def _date_right_btn_cb(self):
        print("date right callback")

    def _date_left_btn_cb(self):
        print("date left callback")

    def _setup_btn_cb(self):
        print("setup callback")

    def _refresh_btn_cb(self):
        print("refresh callback")
