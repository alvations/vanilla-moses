#!/usr/bin/env python -*- coding: utf-8 -*-

import os, sys
from multiprocessing import Process

from utils import run_command

homedir = os.path.expanduser("~")
os.chdir(homedir)

tokdir = 'wmt-data/tok/'
os.makedirs(tokdir, exist_ok=True)

monodir = 'wmt-data/mono/'
paradir = 'wmt-data/parallel'
for lang in os.listdir(monodir):
    cmd = ' '.join('zcat', monodir+lang+'*.gz', '|', 
                   'mosesdecoder/scripts/tokenizer/tokenizer.perl -l', lang, 
                   '>', tokdir+lang+'.all')
    run_command(cmd)
    

