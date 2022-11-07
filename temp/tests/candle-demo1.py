import pandas as pd
import mplfinance as mpf

# Load data file.
df = pd.read_csv('SP500_NOV2019_Hist.csv', index_col=0, parse_dates=True)

# Plot candlestick.
# Add volume.
# Add moving averages: 3,6,9.
# Save graph to *.png.
mpf.plot(df, type='candle', style='charles',
            title='S&P 500, Nov 2019',
            ylabel='Price ($)',
            ylabel_lower='Shares \nTraded',
            volume=True,
            mav=(3,6,9),
            savefig='test-mplfiance.png')
