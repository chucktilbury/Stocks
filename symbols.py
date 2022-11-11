'''
    This module handles the network access related to the actual symbols.
'''

import pandas as pd
import yfinance as yf
from configuration import Config

class Symbol(object):

    def __init__(self, name):
        self.symbol = yf.Ticker(name)
        #print(self.symbol.info)
        self.history = self.symbol.history(period="max", interval="1m")
        self.data = pd.DataFrame(self.history)

        self.config = Config.get_config()

    def name(self):
        return self.symbol.info['symbol']

