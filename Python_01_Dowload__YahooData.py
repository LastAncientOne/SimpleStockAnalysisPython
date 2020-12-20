# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Download stock historical data from Yahoo Finance

import yfinance as yf
yf.pdr_override()


# input
symbol = 'AAPL'
start = '2014-01-01'
end = '2018-01-01'


# dataframe
df = yf.download(symbol,start,end)

# View the first 5 rows
print('First 5 Rows')
print(df.head())
print('-'*80)

# View the last 5 rows
print('Last 5 Rows')
print(df.tail())