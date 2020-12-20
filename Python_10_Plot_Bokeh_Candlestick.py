# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:09:11 2020

@author: Tin
"""
# Plot Candlestick in bokeh
import pandas as pd # Dataframe Library
from math import pi
from bokeh.plotting import figure, show, output_file

pd.set_option('max_columns', None) # To show all columns

import yfinance as yf
yf.pdr_override()


# input
symbol = 'AAPL'
start = '2019-12-01'
end = '2020-01-01'


# dataframe
df = yf.download(symbol,start,end)

df["Date"] = pd.to_datetime(df.index)

mids = (df['Open'] + df['Adj Close'])/2
spans = abs(df['Adj Close']-df['Open'])

inc = df['Adj Close'] > df['Open']
dec = df['Open'] > df['Adj Close']
w = 12*60*60*1000 # half day in ms

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = symbol + " Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3

p.segment(df.Date, df.High, df.Date, df.Low, color="black")
p.vbar(df.Date[inc], w, df.Open[inc], df['Adj Close'][inc], fill_color="#D5E1DD", line_color="black")
p.vbar(df.Date[dec], w, df.Open[dec], df['Adj Close'][dec], fill_color="#F2583E", line_color="black")

output_file("candlestick.html", title= symbol + " candlestick")

show(p)  # open a browser