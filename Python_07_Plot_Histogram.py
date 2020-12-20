# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Plot Histogram Chart
import matplotlib.pyplot as plt
import yfinance as yf
yf.pdr_override()


# input
symbol = 'AAPL'
start = '2019-01-01'
end = '2020-01-01'


# dataframe
data = yf.download(symbol,start,end)

plt.figure(figsize=(14,10))
plt.bar(data.index, data['Adj Close'])
plt.title("Stock Histogram Chart")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

