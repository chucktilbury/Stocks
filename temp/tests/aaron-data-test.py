'''
Resources:  
https://www.statology.org/matplotlib-python-candlestick-chart/
https://blog.quantinsti.com/historical-market-data-python-api/

'''

# Import yfinance and matplotlib and pandas
import yfinance as yf  
import matplotlib.pyplot as plt
import pandas as pd

# Get the data for the stock ticker, start date, and end date
data = yf.download(['TSLA'],'2020-01-01','2022-01-01')

'''
# Plot the close prices
data["Adj Close"].plot()
plt.show()
'''
#Trying out Candlesticks
#pandas dataframe
df = pd.DataFrame(data)

#create the MatPlotLib figure
plt.figure()

#define width of candlestick elements
width=0.4
width2 =0.05

#define up and down prices
up = data[data.Close>=data.Open]
down = data[data.Close<data.Open]

#define colors to use
up_color = 'green'
down_color = 'red'

#plot up prices
plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=up_color)
plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=up_color)
plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=up_color)

#plot down prices
plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=down_color)
plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=down_color)
plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=down_color)

#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')

#display candlestick chart
plt.show()
