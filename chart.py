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

# https://matplotlib.org/stable/api/matplotlib_configuration_api.html
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style

from mplfinance.original_flavor import candlestick_ohlc

import matplotlib.dates as mdates
#import matplotlib.pyplot as plt
#from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
#from mplfinance.original_flavor import candlestick_ohlc

import datetime
import tkinter as tk
import pprint
from configuration import Config


class Chart(tk.Frame):
    '''
    Create a chart to display within a notebook frame.
    '''

    def __init__(self, owner, **kw):

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

        self.config = Config.get_config()
        super().__init__(owner, **kw)
        self.owner = owner
        #self.fname = fname
        #self.start_date = start_date
        #self.end_date = end_date

        # subtract the height of the tab bar
        self.total_height = self.panel_height-105
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
        self.ctl_frame = tk.LabelFrame(self)#, text=name)
        self.ctl_frame.config(width=self.ctl_frame_width)
        self.ctl_frame.config(height=self.total_height)
        self.ctl_frame.grid(row=0, column=1, sticky='nw')

        self.info_frame = tk.LabelFrame(self)#, text='Info')
        self.info_frame.config(width=self.info_frame_width)
        self.info_frame.config(height=self.total_height)
        self.info_frame.grid(row=0, column=2, sticky='nw', padx=7)
        self.info_data_frame = tk.Frame(self.info_frame)
        self.info_data_frame.config(height=self.total_height)
        self.info_data_frame.grid(column=0, row=0)
        btn = tk.Button(self.info_frame, text="Refresh", width=self.btn_width, command=self._refresh_btn_cb)
        btn.grid(column=0, row=1)

        self.grid() # display the frame

    # TODO: split out the logic that actually changes the graph and put it in
    # a different function.
    def create_chart(self, symbol):
        LARGE_FONT= ("Arial", 12)
        style.use("classic")
        # use this for configurations
        # print(style.available)

        data = symbol.history # pd.read_csv(chart)
        # isolate the data from the table
        ohlc = data.iloc[20:50]

        ohlc = ohlc.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
        ohlc['Date'] = pd.to_datetime(ohlc['Date'])
        ohlc['Date'] = ohlc['Date'].apply(mdates.date2num)
        ohlc = ohlc.astype(float)
        #print(ohlc)

        # size of the figure is in inches.
        figure = Figure(figsize=(9.25,5.85), dpi=100)
        figure.suptitle(symbol.name())
        axis = figure.add_subplot(xlabel="Date", ylabel="Price")

        canvas = FigureCanvasTkAgg(figure, self.ctl_frame)
        canvas.get_tk_widget().grid(row=0, column=0)

        candlestick_ohlc(axis, ohlc.values, width=0.6,
                         colorup='green', colordown='red', alpha=0.8)

        date_format = mdates.DateFormatter('%m-%d-%Y')
        axis.xaxis.set_major_formatter(date_format)
        figure.autofmt_xdate()

        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self.ctl_frame, pack_toolbar=False)
        toolbar.update()
        toolbar.grid(row=1, column=0)

    def update_char(self):
        pass

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


'''
        mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
        alldays = DayLocator()              # minor ticks on the days
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        dayFormatter = DateFormatter('%d')      # e.g., 12

        quotes = pd.read_csv(self.fname,
                            index_col=0,
                            parse_dates=True,
                            infer_datetime_format=True)

        # select desired range of dates
        quotes = quotes[(quotes.index >=
                        self.start_date) & (quotes.index <= self.end_date)]

        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        # ax.xaxis.set_minor_formatter(dayFormatter)

        # plot_day_summary(ax, quotes, ticksize=3)
        candlestick_ohlc(ax, zip(mdates.date2num(quotes.index.to_pydatetime()),
                        quotes['Open'], quotes['High'],
                        quotes['Low'], quotes['Close']),
                        width=0.6)

        ax.xaxis_date()
        ax.autoscale_view()
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().grid(row=0, column=0)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.grid(row=1, column=0)

        #plt.setp(plt.gca().get_xticklabels(),
                    #rotation=45, horizontalalignment='right')

'''
