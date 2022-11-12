'''
    This module handles the network access related to the actual symbols.
'''

import pandas as pd
import yfinance as yf
from configuration import Config

class Symbol(object):

    def __init__(self, name):
        self.config = Config.get_config()
        self.symbol = yf.Ticker(name)
        self.history = self.symbol.history(period=self.config.default_period(),
                                            interval=self.config.default_interval())
        self.data = pd.DataFrame(self.history)

    def name(self):
        return self.symbol.info['symbol']

