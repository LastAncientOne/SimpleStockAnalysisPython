# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Modify Yahoo Dataframe Date
import pandas as pd # Dataframe Library
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


# Date becomes a columns
df = data.copy() # Copy the original data
dfn = df.reset_index()
print(dfn.head())
print('-'*80)


# Add Year, Month, Day
df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day
print('Year, Month, & Day')
print(df.head())
print('-'*80)


# Convert Daily to Weekly
weekly = data.copy()
weekly = weekly.resample('W').last()
print('Weekly Data')
print(weekly.head())
print('-'*80)


# Convert Daily to Monthly
monthly = data.copy()
monthly = monthly.resample('1M').mean()
print('Monthly Data')
print(monthly.head())
print('-'*80)


# Choose Particular Year to analyze
monthly = data.copy()
monthly = monthly.reset_index()
y2017 = monthly[monthly['Date'].dt.year==2017]
print("Analyze Particular Year in Historical Data")
print(y2017)
print('-'*80)


month_name = data.copy()
# Convert Daily to Monthly
# 'BMS', which stands for "business month start frequency"
# 'BM', which stands for "business month end frequency"
month_name = month_name.asfreq('BM')
print('Number of the Month')
print(month_name.head())
print('-'*80)


import calendar
month_name['Month_Number'] = month_name.index.month
month_name['Month_ABBR'] = month_name['Month_Number'].apply(lambda x: calendar.month_abbr[x])
print('Abbreviation for Months')
print(month_name.head())
print('-'*80)


print('Month Name')
month_name['Month_Name'] = month_name['Month_Number'].apply(lambda x: calendar.month_name[x])
print(month_name.head())
print('-'*80)


# Pivot Table Date
df_months = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values = 'Adj Close') # each months 
print('Year by Year')
print(df_months)
print('-'*80)


df_days = pd.pivot_table(df, index=df.index.day, columns=df.index.year, values = 'Adj Close') # daily for one whole months
print('Year by Year in daily rows')
print(df_days)
print('-'*80)


df_all_columns = pd.pivot_table(df, index=df.index.month, columns=df.index.year)
print('All columns in yearly')
print(df_all_columns)
print('-'*80)


stock_data = df.copy()
stock_data['Year'] = df.index.year
stock_data['Month'] = df.index.month
stock_data['Day'] = df.index.day
stock_data['Week_Day'] = df.index.dayofweek
stock_data['Week_Day_Name'] = df.index.strftime('%A')
print('Number of day with M-F')
print(stock_data.tail(10))
print('-'*80)


approach1 = stock_data.groupby(['Year', 'Month']).first()['Adj Close']
print('# of Month')
print(approach1.tail(12))
print('-'*80)


approach2 = stock_data.groupby(['Year', 'Day']).first()['Adj Close']
print('# of Day')
print(approach2.tail(12))
print('-'*80)


print('Convert Date to String')
string_date = data.copy()
string_date['Date'] = string_date.index
print(string_date.head())
print('-'*80)


string_date['Date'] = string_date['Date'].dt.strftime("%Y%m%d").astype(int)
print('Convert Date to Numbers')
print(string_date.head())




