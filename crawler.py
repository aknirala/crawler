#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
if sys.version_info[0] == 2:
    import urllib
else:
    import urllib.request
import logging
from collections import defaultdict

url = "http://www.moneycontrol.com/stocks/company_info/stock_news.php?\
sc_id=AT&scat=&pageno=1&next=0&durationType=Y&Year=2015"

if sys.version_info[0] == 2:
    doc = urllib.urlopen(url)
else:
    doc = urllib.request.urlopen(url)

docContent = BeautifulSoup(doc, "html.parser")

articles = []
for element in docContent.find_all("div"):
    try:
        if element.attrs['style'] == "width:550px":
            article = defaultdict(str)
            article_link = "moneycontrol.com" + element.a['href']
            for p in element.find_all('p'):
                if 'a_10dgry' in p.attrs['class']:
                    article_time = p.contents[0].split('|')[0]
                    article_date = p.contents[0].split('|')[1][:-1]
            article['link'] = article_link
            article['time'] = article_time
            article['date'] = article_date
            articles.append(article)
    except:
        logging.debug("div has no width attribute")
