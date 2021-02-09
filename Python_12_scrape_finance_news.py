# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:30:37 2020

@author: Tin
"""
# pip install newspaper3k
import newspaper
from newspaper import Article
 
url = "https://finance.yahoo.com/"
 
# download and parse article
article = Article(url)
article.download()
article.parse()
 
# print article text
print(article.text)

site = newspaper.build("https://finance.yahoo.com/")  
 
# get list of article URLs
print(site.article_urls())

