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
data = yf.download(['TSLA'],'2021-10-01','2022-11-10')

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
df.up = df[df.Close>=df.Open]
df.down = df[df.Close<df.Open]

#define rolling averages
df.sma8 = df.Close.rolling(window=8).mean()
df.sma10 = df.Close.rolling(window=10).mean()

#find the points that are above and below the running average, then plot them as points

buy= df[df.Close>df.sma8]
sell= df[df.Close<df.sma8]
plt.scatter(x=buy.index,y=buy.Close)
plt.scatter(x=sell.index,y=sell.Close)



#define colors to use
up_color = 'green'
down_color = 'red'

#plot up prices
plt.bar(df.up.index,df.up.Close-df.up.Open,width,bottom=df.up.Open,color=up_color)
plt.bar(df.up.index,df.up.High-df.up.Close,width2,bottom=df.up.Close,color=up_color)
plt.bar(df.up.index,df.up.Low-df.up.Open,width2,bottom=df.up.Open,color=up_color)

#plot down prices
plt.bar(df.down.index,df.down.Close-df.down.Open,width,bottom=df.down.Open,color=down_color)
plt.bar(df.down.index,df.down.High-df.down.Open,width2,bottom=df.down.Open,color=down_color)
plt.bar(df.down.index,df.down.Low-df.down.Close,width2,bottom=df.down.Close,color=down_color)

#plot rolling averages
plt.plot(df.sma8,'blue',label='SMA8')
plt.plot(df.sma10,'purple',label='SMA10')
#plt.fill_between(data.Close.index,df.sma8,df.sma10, color='y',alpha=0.1)

#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')

#display candlestick chart
plt.show()

#print(df.info())