from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import pyplot as plt
from datetime import datetime as dt
import numpy as np



def candle_plot(df_ohlc, numb_days, symb, descr, candle_width):
    # reduce the data set to the date range of interest
    df_latest = df_ohlc.tail(numb_days)


    # set up the plot
    fig, ax = plt.subplots(figsize=(10,7))
    fig.subplots_adjust(bottom=0.3)
    ax.grid(which='major', axis='y', linestyle='--')


    # run the candle plot
    candlestick_ohlc(ax, df_latest.open, df_latest.high, df_latest.low, df_latest.close,
                        width=.9, colorup='g');


    # reset the df index to match that of the ax and plot the moving averages
    df_latest.index = np.arange(len(df_latest.index))
    ax.plot('sma20', data=df_latest, color='limegreen', linewidth=1)
    ax.plot('sma50', data=df_latest, color='orangered', linewidth=1)
    ax.plot('sma200', data=df_latest, color='red', linewidth=1)


    # add the legend
    ax.legend(ncol=3, bbox_to_anchor=(0,0.9), loc='lower left')


    # remove the bottom axis ticks and labels
    plt.tick_params(axis='x', bottom=False, labelbottom=False)


    # add the ticker label
    ax.text(0, 1.08, symb, horizontalalignment='left', verticalalignment='bottom',
        transform=ax.transAxes, fontsize=20, fontweight='bold')


    # add the company name
    ax.text(0, 1.02, descr, horizontalalignment='left', verticalalignment='bottom',
        transform=ax.transAxes, fontsize=16, color='dimgrey')


    # add the performance header
    ax.text(1, 1.08, '{} day performance:'.format(numb_days), horizontalalignment='right',
            verticalalignment='bottom', transform=ax.transAxes, fontsize=14, style='italic',
            color='dimgrey')


    # add the performance label
    perf = round((df_latest['close'].values[-1]/df_latest['close'].values[0]) - 1, 4)
    perfLabel = '{:.2%}'.format(perf)
    perfColor = 'green' if perf > 0 else 'red'
    ax.text(1, 1.02, perfLabel, horizontalalignment='right', verticalalignment='bottom',
        transform=ax.transAxes, fontsize=16, color=perfColor, fontweight='bold')


    # add the bottom axis date range labels
    minDate = df_latest['tradeDate'].min().strftime('%m/%d/%Y')
    maxDate = df_latest['tradeDate'].max().strftime('%m/%d/%Y')
    ax.text(0, -0.02, minDate, horizontalalignment='left', verticalalignment='top',
        transform=ax.transAxes, fontsize=12, color='dimgrey')
    ax.text(1, -0.02, maxDate, horizontalalignment='right', verticalalignment='top',
        transform=ax.transAxes, fontsize=12, color='dimgrey')

candle_plot()
