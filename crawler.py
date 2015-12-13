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
import json
from boilerpipe.extract import Extractor

months = {"Jan": "1", "Feb": "2", "Mar": "3",
          "Apr": "4", "May": "5", "Jun": "6",
          "Jul": "7", "Aug": "8", "Sep": "9",
          "Oct": "10", "Nov": "11", "Dec": "12"}

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
            article_link = "http://www.moneycontrol.com" + element.a['href']
            for p in element.find_all('p'):
                if 'a_10dgry' in p.attrs['class']:
                    article_time = p.contents[0].split('|')[0]
                    article_date = p.contents[0].split('|')[1][:-1]
            article['link'] = article_link
            article['time'] = article_time
            article['date'] = article_date

            extractor = Extractor(extractor='ArticleExtractor',
                                  url=article_link)
            article['content'] = extractor.getText()
            if sys.version_info[0] == 2:
                article_doc = urllib.urlopen(article_link)
            else:
                article_doc = urllib.request.urlopen(url)
            article['title'] = BeautifulSoup(extractor.getHTML(),
                                             "html.parser").find_all(
                                                 "h1")[0].contents[0]
            articles.append(article)
    except:
        logging.debug("div has no width attribute")

if len(articles):
    for article in articles:
        date = article['date'].split()
        filename = ''.join([date[2], months[date[1]], date[0], '.json'])
        with open(filename, 'w') as outfile:
            json.dump(articles, outfile)
