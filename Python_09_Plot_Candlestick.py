# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Plot Candlestick in Matplotlib
import pandas as pd # Dataframe Library
import matplotlib.pyplot as plt # Plot Chart Library

pd.set_option('max_columns', None) # To show all columns

import yfinance as yf
yf.pdr_override()


# input
symbol = 'AAPL'
start = '2019-01-01'
end = '2020-01-01'


# dataframe
data = yf.download(symbol,start,end)

data['VolumePositive'] = data['Open'] < data['Adj Close']

print('Line Chart')
fig = plt.figure(figsize=(14,10))
ax1 = plt.subplot(3, 1, 1)
ax1.plot(data['Adj Close'])
ax1.set_title('Stock '+ symbol +' Closing Price')
ax1.set_ylabel('Price')
ax1.legend(loc='best')

ax2 = plt.subplot(3, 1, 2)
ax2.plot(data['Volume'], label='Volume')
ax2.grid()
ax2.legend(loc='best')
ax2.set_ylabel('Volume')

ax3 = plt.subplot(3, 1, 3)
ax3v = ax3.twinx()
colors = data.VolumePositive.map({True: 'g', False: 'r'})
ax3v.bar(data.index, data['Volume'], color=colors, alpha=0.4)
ax3.set_ylabel('Volume')
ax3.grid()
ax3.set_xlabel('Date')


# Candlestick
print('Candlestick')
from matplotlib import dates as mdates
dfc = data.copy()
dfc['VolumePositive'] = dfc['Open'] < dfc['Adj Close']
#dfc = dfc.dropna()
dfc = dfc.reset_index()
dfc['Date'] = pd.to_datetime(dfc['Date'])
dfc['Date'] = dfc['Date'].apply(mdates.date2num)
dfc.head()

from mpl_finance import candlestick_ohlc

fig = plt.figure(figsize=(14,10))
ax1 = plt.subplot(3, 1, 1)
candlestick_ohlc(ax1,dfc.values, width=0.5, colorup='g', colordown='r', alpha=1.0)
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
ax1.grid(True, which='both')
ax1.minorticks_on()
ax1v = ax1.twinx()
colors = dfc.VolumePositive.map({True: 'g', False: 'r'})
ax1v.bar(dfc.Date, dfc['Volume'], color=colors, alpha=0.4)
ax1v.axes.yaxis.set_ticklabels([])
ax1v.set_ylim(0, 3*data.Volume.max())
ax1.set_title('Stock '+ symbol +' Closing Price')
ax1.set_ylabel('Price')

ax2 = plt.subplot(3, 1, 2)
ax2.plot(data['Volume'], label='Volume')
ax2.grid()
ax2.legend(loc='best')
ax2.set_ylabel('Volume')

ax3 = plt.subplot(3, 1, 3)
ax3v = ax3.twinx()
colors = data.VolumePositive.map({True: 'g', False: 'r'})
ax3v.bar(data.index, data['Volume'], color=colors, alpha=0.4)
ax3.set_ylabel('Volume')
ax3.grid()
ax3.set_xlabel('Date')
