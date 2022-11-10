'''
    This module handles the network access related to the actual symbols.
'''

import pandas as pd
import yfinance as yf

class Symbol(object):

    def __init__(self, name):
        self.symbol = yf.Ticker(name)
        #print(self.symbol.info)
        self.history = self.symbol.history(period="max", interval="1m")
        self.data = pd.DataFrame(self.history)

    def name(self):
        return self.symbol.info['symbol']

import pickle

# TODO: handle exceptions
def save(obj, name):
    with open(name, "wb") as fh:
        pickle.dump(obj, fh, fix_imports=True)

def load(name):
    with open(name, "rb") as fh:
        obj = pickle.load(fh, fix_imports=True)
    return obj


if __name__ == "__main__":

    sym = Symbol("MSFT")
    save(sym, "test-pickle.pkl")
    obj = load("test-pickle.pkl")
    print(obj.name())
