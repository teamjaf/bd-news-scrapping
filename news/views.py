from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
# GEtting news from The News Standard

toi_r = requests.get("https://www.tbsnews.net/")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h3')

toi_headings = toi_headings[0:-20] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from The Daily Star

ds_r = requests.get("https://www.thedailystar.net/english")
ds_soup = BeautifulSoup(ds_r.content, 'html5lib')
ds_soup.getText()

ds_headings = ds_soup.find_all('h3')

ds_headings = ds_headings[0:-13] # removing footers

ds_news = []

for ds in ds_headings:
    ds_news.append(ds.text)




#Getting news from The Dhaka Tribue
#
# dt_r = requests.get("https://www.theindependentbd.com/")
# dt_soup = BeautifulSoup(dt_r.content, 'html5lib')
# dt_soup.getText()
#
# dt_headings = dt_soup.find_all('h3')
#
# dt_headings = dt_headings[0:-13] # removing footers
#
# dt_news = []
#
# for dt in dt_headings:
#     dt_news.append(dt.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ds_news, })

dicitonary = {'TBS Headings': toi_headings, 'The Daily Star': ds_soup}
df = pd.DataFrame.from_dict(dicitonary, orient='index')
to_csv = df.to_csv ('C:/Users/Administrator/Desktop/news_data.csv')
df = df.transpose()
