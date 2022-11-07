# original source for this is "finance_demo.py" in the mplfinance repository
# in the examples/original_flavor directory.

import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
import os.path

# candlestick_ohlc may be deprecated. Cannot really find docs for it that say
# one way or another. We may want to include these libraries as part of our own
# app in order to preserve compatibility.
from mplfinance.original_flavor import candlestick_ohlc

# yfinance is the easiest data-getter to use. I don't know where the data is
# coming from. There once was a thing called Yahoo Finance, but it has been
# discontinued. There are other getters, but they are not free and/or are a lot
# harder to use.
import yfinance as yf

#date1 = "2004-2-1"
#date2 = "2004-4-12"
# pick a two month window in the big block of data. In practice, this will be a
# window that is set by the user in a configuration.
date1 = "2021-01-04"
date2 = "2021-02-26"

# get the data from the internet. This can be already saved as a CSV, but I am
# reloading it for the sake of completeness.
data = yf.download()

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

#infile = os.path.join('data','yahoofinance-INTC-19950101-20040412.csv')
#infile = os.path.join('data','test.csv')
#quotes = pd.read_csv(infile,
quotes = pd.read_csv('test.csv',
                     index_col=0,
                     parse_dates=True,
                     infer_datetime_format=True)

# select desired range of dates
quotes = quotes[(quotes.index >= date1) & (quotes.index <= date2)]

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
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()
