from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

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


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ds_news})