# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Plot Line Charts
import pandas as pd # Dataframe Library
import matplotlib.pyplot as plt # Plot Chart Library

pd.set_option('max_columns', None) # To show all columns

import yfinance as yf
yf.pdr_override()


# input
symbol = 'AAPL'
start = '2014-01-01'
end = '2018-01-01'


# dataframe
data = yf.download(symbol,start,end)

# View the first 5 rows
print('First 5 Rows')
print(data.head())
print('-'*80)

print('Line Chart')
plt.figure(figsize=(12,8))
plt.plot(data['Adj Close'])
plt.title("Stock Line Chart")
plt.legend(loc='best')
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
print('-'*80)


print('Line Chart with Grid')
plt.figure(figsize=(12,8))
plt.plot(data['Adj Close'])
plt.title("Stock Line Chart")
plt.grid()
plt.legend(loc='best')
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
print('-'*80)


print('Render the grid')
fig, ax = plt.subplots()
data.plot(kind='line', y= 'Adj Close', ax=ax)
# Turn on the grid
ax.grid()
plt.title("Stock Line Chart")
plt.legend(loc='best')
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
print('-'*80)


print('Customize the grid')
fig, ax = plt.subplots()
data.plot(kind='line', y= 'Adj Close', ax=ax)
# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)
# Customize the grid
ax.grid(linestyle='-', linewidth='0.5', color='red')
plt.title("Stock Line Chart")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
print('-'*80)


print('Major grid & Minor Grid')
plt.figure(figsize=(12,8))
plt.plot(data['Adj Close'])
plt.minorticks_on()
plt.grid(b=True, which='major', color='b', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.title("Stock Line Chart")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
print('-'*80)


import seaborn as sns # Plot Library 0.9.0 Version
# conda install -c anaconda seaborn=0.9.0
plt.figure(figsize=(10,5))
sns.lineplot(data=data, x=data.index, y='Adj Close')
print('-'*80)

plt.figure(figsize=(10,5))
top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)
bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
top.plot(data.index, data['Adj Close']) 
bottom.bar(data.index, data['Volume']) 
 
# set the labels
top.axes.get_xaxis().set_visible(False)
top.set_title('Stock Price and Volume')
top.set_ylabel('Adj Closing Price')
bottom.set_ylabel('Volume')
print('-'*80)


# Candlestick
from mpl_finance import candlestick_ohlc
from matplotlib import dates as mdates

# Converting date to pandas datetime format
dfc = data.copy()
dfc = dfc.reset_index()
dfc['Date'] = pd.to_datetime(dfc['Date'])
dfc['Date'] = dfc['Date'].apply(mdates.date2num)
# dfc.head()

fig = plt.figure(figsize=(14,10))
ax1 = plt.subplot(2, 1, 1)
candlestick_ohlc(ax1,dfc.values, width=0.5, colorup='g', colordown='r', alpha=1.0)
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
ax1.set_title('Stock '+ symbol +' Closing Price')
ax1.set_ylabel('Price')




import plotly.graph_objs as go
# from plotly.offline import init_notebook_mode, iplot

df = data.copy()
# Plot OHLC Bar Chart
trace = go.Ohlc(x=df['12-2016'].index,
                open=df['12-2016'].Open,
                high=df['12-2016'].High,
                low=df['12-2016'].Low,
                close=df['12-2016'].Close)
data = [trace]
iplot(data, filename='simple_ohlc')
