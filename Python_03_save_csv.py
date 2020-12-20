# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:55:42 2020

@author: Tin
"""
# Save Data to CSV
import warnings
warnings.filterwarnings("ignore")

import yfinance as yf
yf.pdr_override()

# input
symbol = 'AMD'
start = '2014-01-01'
end = '2019-01-01'

# Read data 
data = yf.download(symbol,start,end)

# Output data into CSV
# To save in your certain folder, change the Users name
data.to_csv("C:/Users/Finance/Desktop/AMD.csv")



symbols = ['PFE','TGT','MA','UNH','VZ','V','WMT','GS']
start = '2014-01-11' 
end = '2019-01-01'
stocks_info = yf.download(symbols, start, end)['Adj Close']
stocks_data = stocks_info.iloc[::]
print(stocks_data)

# Output data into CSV
stocks_data.to_csv("C:/Users/Finance/Desktop/stocks_data.csv")
