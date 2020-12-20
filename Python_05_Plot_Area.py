# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Plot Area Chart
import matplotlib.pyplot as plt
import pandas as pd 

pd.set_option('max_columns', None) # To show all columns

import yfinance as yf
yf.pdr_override()


# input
symbol = 'AAPL'
start = '2019-01-01'
end = '2020-01-01'


# dataframe
data = yf.download(symbol,start,end)

print('Plot Histogram Chart')
plt.figure(figsize=(12,8))
data['Adj Close'].plot.area()
plt.title("Stock Area Chart")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()


data[['Open','High','Low','Adj Close']].plot.area(stacked=False)
plt.title("Stock Area Chart")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(loc='best')
plt.show()