#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import os
import urllib.request
from collections import defaultdict

from boilerpipe.extract import Extractor
from bs4 import BeautifulSoup


def get_articles(url):
    doc = urllib.request.urlopen(url)
    docContent = BeautifulSoup(doc, 'html.parser')
    articles = []
    for element in docContent.find_all('div'):
        try:
            if element.attrs['style'] == 'width:550px':
                article = defaultdict(str)
                article_link = 'http://www.moneycontrol.com' + element.a['href']
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
                        article['title'] = BeautifulSoup(extractor.getHTML(),
                                                         'html.parser').find_all('h1')[0].contents[0]
                        articles.append(article)
                        break
        except:
            logging.debug('div has no width attribute')
    return articles


def main():
    main_url = 'http://www.moneycontrol.com/stocks/company_info/stock_news.php?'
    param_list = ['sc_id', 'pageno', 'durationType', 'Year']

    # list of company IDs from moneycontrol.com
    sc_ids = {'AT': 'Apollo Tyres',
              'SE17': 'Suzlon Energy',
              'NI': 'Nestle India',
              }

    year_range = ['2015', '2014']
    pages = range(1, 10)

    for sc_id, name in sc_ids.items():
        articles = []
        for year in year_range:
            for page in pages:
                param = '&'.join(['{}={}'.format(a, b)
                                  for a, b in zip(param_list, [sc_id, page, 'Y', year])])
                url = main_url + param
                print(url)
                articles.append(get_articles(url))
        if articles:
            filename = os.path.join('data', ''.join([name, '.json']))
            # save all the articles of a particular company in a file labled CompanyName.json
            with open(filename, 'w') as outfile:
                json.dump(articles, outfile)

main()
