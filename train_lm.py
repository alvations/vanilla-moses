#!/usr/bin/env python -*- coding: utf-8 -*-

import os, sys
from multiprocessing import Process

from utils import run_command, parallized_run_command
import wmt_data

homedir = os.path.expanduser("~")
os.chdir(homedir)

def tokenize_monolingual_data(langs=None):
    homedir = os.path.expanduser("~")
    os.chdir(homedir)
    tokdir = homedir + '/wmt-data/tok/'
    os.makedirs(tokdir, exist_ok=True)
    
    monodir = 'wmt-data/mono/'
    paradir = 'wmt-data/parallel'
    cmds = []
    for _lang in os.listdir(monodir):
        if langs is not None and _lang not in langs:
            continue
        if os.path.exists(tokdir+_lang+'.all'):
            continue
        cmd = ' '.join(['zcat', monodir+_lang+'/*.gz', '|', 
                       'mosesdecoder/scripts/tokenizer/tokenizer.perl -threads 10 -l', _lang, 
                       '>', tokdir+_lang+'.all'])
        cmds.append(cmd)
        
    parallized_run_command(cmds, 10)

def train_language_model(n=6, langs=None):
    homedir = os.path.expanduser("~")
    os.chdir(homedir)
    lmdir = homedir + '/wmt-data/lm/'
    os.makedirs(lmdir, exist_ok=True)
    for _lang in os.listdir(tokdir):
        if langs is not None and _lang not in langs:
            continue
        if os.path.exists(lmdir+ 'lm.'+n+'gram.'+_lang+'.arpa.gz'):
            continue
        cmd = 'mosesdecoder/bin/lmplz --order ' + n + ' -S 80% -T /tmp <'
        cmd+= lmdir + _lang + '.all '
        cmd+= '| gzip > ' + lmdir+ 'lm.'+n+'gram.'+_lang+'.arpa.gz'
        run_command(cmd)
        
if __name__ == '__main__':
    # Download all data.
    if len(sys.argv) == 1:
        tokenize_monolingual_data()
        #train_language_model()
    if len(sys.argv) > 1:
        sysargv = sys.argv[1:]
        n, langs = sysargv[1], sysargv[2:]
        assert int(sysargv[1])
        if langs == []:
            tokenize_monolingual_data()
            #train_language_model(n)
        else:
            assert all(l for l in langs if l in wmt_data.wmtlangs)
            tokenize_monolingual_data(langs)
            #train_language_model(n, langs)
             