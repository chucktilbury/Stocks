# This one simply gets the whole history of Microsoft stock and saves it as a
# CSV file. This also demonstrates getting other types of data that could be
# useful for other calculations.
# Source: https://stackoverflow.com/questions/65875169/how-to-use-yahoo-finance-market-data-downloader-yfinance-python-package-from

import yfinance as yf
import pandas as pd
symbol = "DFIC"
ticker = yf.Ticker(symbol)

# get stock info
ticker.info
print(ticker.info)

# get historical market data
hist = ticker.history(period="max", interval="1m")
print(hist)
df = pd.DataFrame(hist)
df.to_csv(symbol+'-max-1m.csv')

'''
# show actions (dividends, splits)
msft.actions
print(msft.actions)

# show dividends
msft.dividends
print(msft.dividends)

# show splits
msft.splits
print(msft.splits)

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
opt = msft.option_chain('2021-01-29')
# data available via: opt.calls, opt.puts
'''
