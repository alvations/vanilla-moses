#!/usr/bin/env python -*- coding: utf-8 -*-

import os, sys
from multiprocessing import Process

homedir = os.path.expanduser("~")
os.chdir(homedir)

monodir = 'wmt-data/mono/'
paradir = 'wmt-data/parallel'
for i in os.listdir(monodir):
    print(monodir + i)