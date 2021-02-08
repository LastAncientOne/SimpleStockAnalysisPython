# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:30:37 2020

@author: Tin
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.yahoo.com/quote/AMD/key-statistics?p=AMD')
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]

print(df)