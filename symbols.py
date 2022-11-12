'''
    This module handles the network access related to the actual symbols.
'''
import pandas as pd
import yfinance as yf
import datetime as dt
from configuration import Config

class Symbol(object):

    def __init__(self, name):
        self.config = Config.get_config()
        self.get_ticker(name, interval='1d')
        self.interval = None
        self.period = None

    def name(self):
        return self.ticker.info['symbol']

    def _convert_history(self, history):
        '''
        convert and return a pd.DataFrame that is ready to plot using
        mlpfinancial.condlestick_ohlc().
        '''
        csv = history.to_csv()
        rows = csv.split("\n")

        names = rows[0].split(",")
        if names[0] != "Date":
            names[0] = "Date"

        output = {}
        for name in names:
            output[name] = []

        # delete the first line with the labels
        del rows[0]
        for tmp in rows:
            row = tmp.split(",")

            # do not process short or blank lines
            if len(row) == len(names):
                for idx, item in enumerate(row):
                    if(names[idx] != "Date"):
                        output[names[idx]].append(float(item))
                    else:
                        output[names[idx]].append(item)

        return pd.DataFrame(output)

    def get_ticker(self, name, period='max', interval='1m', start=None, end=None):
        '''
        Get the ticker and history from the internet as a tuple.

        valid periods: "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y",
        "5y", "10y", "ytd", "max"

        valid intervals: "1m", "2m", "5m", "15m", "30m", "60m", "90m",
        "1h", "1d", "5d", "1wk", "1mo", "3mo"

        date format for start and end: 'yyyy-mm-dd'

        Source: https://algotrading101.com/learn/yfinance-guide/
        '''
        self.ticker = yf.Ticker(name)
        # actions=false causes only open, close, high and low to be gotten
        if not start is None and not end is None:
            history = self.ticker.history(start=start, end=end, interval=interval, actions=False)
        else:
            history = self.ticker.history(period=period, interval=interval, actions=False)

        self.history = self._convert_history(history)
        return (self.history, self.ticker)
