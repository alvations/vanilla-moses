#!/usr/bin/env python -*- coding: utf-8 -*-

import subprocess
import os

def parallelized_download(command, files, arguments="", max_processes=2):
    processes = set()
    for name in files:
        processes.add(subprocess.call([command, name, arguments],
                                       stdout=open(os.devnull, 'wb')))
        if len(processes) >= max_processes:
            os.wait()