# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Plot Boxplot Chart
import pandas as pd # Dataframe Library
import matplotlib.pyplot as plt # Plot Chart Library

pd.set_option('max_columns', None) # To show all columns

import yfinance as yf
yf.pdr_override()


# input
symbol = 'AAPL'
start = '2019-12-01'
end = '2020-01-01'


# dataframe
data = yf.download(symbol,start,end)

plt.figure(figsize=(14,8))
plt.boxplot(data['Adj Close'])
plt.xlabel("Month of December")
plt.ylabel("Price")
plt.show()