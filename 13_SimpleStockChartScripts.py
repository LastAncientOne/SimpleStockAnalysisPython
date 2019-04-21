# Library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

# fix_yahoo_finance is used to fetch data 
import fix_yahoo_finance as yf
yf.pdr_override()

# input
symbol = 'AAPL' # Pick Symbol
start = '2018-12-01' # Pick Starting Date
end = '2019-01-01' # Pick Ending Date

df = yf.download(symbol,start,end)

# Plot Charts
plt.figure(figsize=(12,8))
plt.plot(df['Adj Close'])
plt.title("Stock Line Chart")
plt.legend(loc='best')
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
