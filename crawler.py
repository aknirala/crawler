# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
# from IPython.display import Image
import urllib

url="http://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=AT&scat=&pageno=1&next=0&durationType=Y&Year=2015"



doc = urllib.urlopen(url)

docContent = BeautifulSoup(doc, "html.parser")

for link in docContent.find_all("a"):
    try:
        if link.attrs['class'] == [u'g_14bl']:
            #print link.get("href")
            pass
    except:
        pass

for paragraph in docContent.find_all("p"):
    try:
        if paragraph.attrs['class'] == ["PT3", "a_10dgry"]:
            print paragraph.contents[0].split('|')[0]
            print paragraph.contents[0].split('|')[1][:-1]
    except:
        pass
#print docContent
