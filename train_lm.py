#!/usr/bin/env python -*- coding: utf-8 -*-

import os, sys
from multiprocessing import Process

homedir = os.path.expanduser("~")
os.chdir(homedir)

for i in os.listdir('wmt-data'):
    print(i)