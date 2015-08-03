#!/usr/bin/env python -*- coding: utf-8 -*-

import os

import wmt_data 
from utils import parallelized_commandline

def download_wmt_monolingual(lang, maxp=5):
    langdir = 'data/mono/' + lang + '/'
    os.makedirs(langdir, exist_ok=True)
    os.chdir(langdir)
    _urls = wmt_data.monolingual[lang]
    parallelized_commandline('wget', _urls, max_processes=maxp)
    os.chdir('../../..')


def download_wmt_parallel(corpus_name, maxp=5):    
    corpusdir = 'data/parallel/' + corpus_name + '/'
    os.makedirs(corpusdir, exist_ok=True)
    os.chdir(corpusdir)
    url = wmt_data.parallel[corpus_name]
    parallelized_commandline('wget', [url])
    os.chdir('../../..')

for corpus_name in wmt_data.parallel:    
    download_wmt_parallel(corpus_name)
    break

'''
http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz
http://www.statmt.org/wmt15/europarl-v8.fi-en.tgz
http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz
http://www.statmt.org/wmt13/training-parallel-un.tgz
http://www.statmt.org/wmt15/training-parallel-nc-v10.tgz
http://www.statmt.org/wmt10/training-giga-fren.tar
http://www.statmt.org/wmt15/wiki-titles.tgz
'''



