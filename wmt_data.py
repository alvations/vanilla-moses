#!/usr/bin/env python -*- coding: utf-8 -*-

import os
import urllib.request
from collections import defaultdict

from bs4 import BeautifulSoup

wmt15_page = 'http://www.statmt.org/wmt15/translation-task.html'
wmt15_soup = BeautifulSoup(urllib.request.urlopen(wmt15_page).read())

wmtlangs = ['cs', 'de', 'en', 'fi', 'fr', 'ru', 'es']

'''
# Code to get the static lang2mono.
lang2mono = defaultdict(list)
urls = [i.get('href') for i in wmt15_soup.find_all('a') 
        if str(i.get('href')).endswith('.gz')]
for j in urls:
    lang = next(l for l in j.split('.') if l in wmtlangs)
    lang2mono[lang].append('http://www.statmt.org/wmt15/'+j)
print(lang2mono)
'''

monolingual = {
'en': ['http://www.statmt.org/wmt15/../wmt14/training-monolingual-europarl-v7/europarl-v7.en.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-nc-v10/news-commentary-v10.en.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2008.en.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2009.en.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2010.en.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2011.en.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2012.en.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2013.en.shuffled.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl-v2/news.2014.en.shuffled.v2.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl/news.2014.en.shuffled.gz', 
       'http://www.statmt.org/wmt15/news-discuss-v1.en.txt.gz'],
              
'ru': ['http://www.statmt.org/wmt15/training-monolingual-nc-v10/news-commentary-v10.ru.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2008.ru.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2009.ru.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2010.ru.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2011.ru.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2012.ru.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2013.ru.shuffled.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl-v2/news.2014.ru.shuffled.v2.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl/news.2014.ru.shuffled.gz'],
              
'de': ['http://www.statmt.org/wmt15/../wmt14/training-monolingual-europarl-v7/europarl-v7.de.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-nc-v10/news-commentary-v10.de.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2008.de.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2009.de.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2010.de.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2011.de.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2012.de.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2013.de.shuffled.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl-v2/news.2014.de.shuffled.v2.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl/news.2014.de.shuffled.gz'], 
             
'fr': ['http://www.statmt.org/wmt15/../wmt14/training-monolingual-europarl-v7/europarl-v7.fr.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-nc-v10/news-commentary-v10.fr.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2008.fr.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2009.fr.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2010.fr.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2011.fr.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2012.fr.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2013.fr.shuffled.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl-v2/news.2014.fr.shuffled.v2.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl/news.2014.fr.shuffled.gz', 
       'http://www.statmt.org/wmt15/news-discuss-v1.fr.txt.gz'],
              
'fi': ['http://www.statmt.org/wmt15/training-monolingual-news-crawl-v2/news.2014.fi.shuffled.v2.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl/news.2014.fi.shuffled.gz'], 
             
'cs': ['http://www.statmt.org/wmt15/../wmt14/training-monolingual-europarl-v7/europarl-v7.cs.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-nc-v10/news-commentary-v10.cs.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2007.cs.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2008.cs.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2009.cs.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2010.cs.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2011.cs.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2012.cs.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2013.cs.shuffled.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl-v2/news.2014.cs.shuffled.v2.gz', 
       'http://www.statmt.org/wmt15/training-monolingual-news-crawl/news.2014.cs.shuffled.gz'],

'es': ['http://www.statmt.org/wmt15/training-monolingual-nc-v10/news-commentary-v10.es.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2007.es.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2008.es.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2009.es.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2010.es.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2011.es.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2012.es.shuffled.gz', 
       'http://www.statmt.org/wmt15/../wmt14/training-monolingual-news-crawl/news.2013.es.shuffled.gz',
      ]


}


parallel = {
'europarl-v7':'http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz',
'europarl-v8':'http://www.statmt.org/wmt15/europarl-v8.fi-en.tgz',
'commoncrawl':'http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz',
'UN':'http://www.statmt.org/wmt13/training-parallel-un.tgz',
'news-commentary':'http://www.statmt.org/wmt15/training-parallel-nc-v10.tgz',
'news-commentary-wmt13':'http://www.statmt.org/wmt13/training-parallel-nc-v8.tgz'
'giga-fren':'http://www.statmt.org/wmt10/training-giga-fren.tar',
'wiki-titles':'http://www.statmt.org/wmt15/wiki-titles.tgz'}


parallel_langs = {
'de':['europarl-v7', 'commoncrawl', 'news-commentary'],
'cs':['europarl-v7', 'commoncrawl', 'news-commentary'],
'fi':['europarl-v8', 'wiki-titles'],
'fr':['europarl-v7', 'commoncrawl', 'news-commentary', 'UN', 'giga-fren'],
'ru':['commoncrawl', 'news-commentary', 'wiki-titles'],
'es':['europarl-v7', 'commoncrawl', 'news-commentary-wmt13'],
}
                 
