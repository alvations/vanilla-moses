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

def train_language_model(n=6, langs=None, parallelized=False):
    homedir = os.path.expanduser("~")
    os.chdir(homedir)
    lmdir = homedir + '/wmt-data/lm/'
    tokdir = homedir + '/wmt-data/tok/'
    os.makedirs(lmdir, exist_ok=True)
    
    cmds = []
    for _lang in os.listdir(tokdir):
        if langs is not None and _lang not in langs:
            continue
        if os.path.exists(lmdir+ 'lm.'+str(n)+'gram.'+_lang[:-4]+'.arpa.gz'):
            continue
        cmd = 'mosesdecoder/bin/lmplz --order ' + str(n) + ' -S 80% -T /tmp <'
        cmd+= tokdir + _lang
        cmd+= '| gzip > ' + lmdir+ 'lm.'+str(n)+'gram.'+_lang[:-4]+'.arpa.gz'
        cmds.append(cmd)

    for cmd in cmds:
        run_command(cmd)
    #parallized_run_command(cmds, 10)

if __name__ == '__main__':
    # Download all data.
    sysargv = sys.argv
    if len(sysargv) == 1:
        tokenize_monolingual_data()
        train_language_model()
    if len(sysargv) == 2:
        sysargv = sys.argv
        n = sysargv[1]
        assert int(sysargv[1])
        tokenize_monolingual_data()
        train_language_model(n)