
'''
    This module converts a yfinance history to a dictionary suitable for
    the candlestick style graphic.
'''
import pandas as pd
import yfinance as yf
import datetime as dt

def convert_time(time_str):

    # convert the time string to python format
    tmp = time_str.split("-")
    # rebuild the string
    val = tmp[0] + "-" + tmp[1] + "-" + tmp[2]
    val = dt.datetime.strptime(val, '%Y-%m-%d %H:%M:%S')

    return val.timestamp()

def convert_history(history):
    '''
    convert and return a pd.DataFrame that is ready to plot using
    mlpfinancial.condlestick_ohlc().
    '''

    # convert the DataFrame to a CSV string
    csv = history.to_csv()

    # Do the convert
    # Split on the '\n'
    rows = csv.split("\n")

    # Now the s1[0] is the comma separated labels. THese are
    # going to be the names in the dictionary.
    names = rows[0].split(",")
    if names[0] != "Date":
        names[0] = "Date"

    # Initialize a dictionary for the output
    output = {}

    # assign an array to each name
    for name in names:
        output[name] = []

    # delete the first line with the labels
    del rows[0]

    # Now iterate all of the rows and store the data as an array
    # in the dictionary. The first row is the labels.
    for tmp in rows:
        # split the row into an array of strings
        row = tmp.split(",")

        # do not process short or blank lines
        if len(row) == len(names):
            #print(row)
            for idx, item in enumerate(row):
                if(names[idx] != "Date"):
                    #print(item)
                    output[names[idx]].append(float(item))
                else:
                    # clip the date and discard the time
                    output[names[idx]].append(convert_time(item))

    # convert the output back to a pandas.DataFrame
    output = pd.DataFrame(output)
    # strip the volume column
    output = output.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]

    return output

def get_data(name, period='max', interval='1m', start=None, end=None):
    '''
    Get the ticker and history from the internet as a tuple.

    valid periods: "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y",
    "5y", "10y", "ytd", "max"

    valid intervals: "1m", "2m", "5m", "15m", "30m", "60m", "90m",
    "1h", "1d", "5d", "1wk", "1mo", "3mo"

    date format for start and end: 'yyyy-mm-dd'

    Source: https://algotrading101.com/learn/yfinance-guide/
    '''
    # make the ticker and get the history
    ticker = yf.Ticker(name)
    # actions=false causes only open, close, high and low
    # to be gotten
    if not start is None and not end is None:
        history = ticker.history(start=start, end=end, interval=interval, actions=False)
    else:
        history = ticker.history(period=period, interval=interval, actions=False)

    return (convert_history(history), ticker)

if __name__ == '__main__':

    #history, ticker = get_data("MSFT", period='3mo', interval='1wk')
    # Note that these dates are not actually returned, but they work anyhow.
    history, ticker = get_data("MSFT", start='2021-01-01', end='2022-01-01', interval='1wk')

    print(history)
