#!/usr/bin/env python -*- coding: utf-8 -*-

import subprocess
import os

def parallelized_commandline(command, files, arguments="", max_processes=2):
    processes = set()
    for name in files:
        processes.add(subprocess.call([command, name, arguments],
                                       stdout=open(os.devnull, 'wb')))
        if len(processes) >= max_processes:
            os.wait()
            processes.difference_update(
                [p for p in processes if p.poll() is not None])
            
    #Check if all the child processes were closed
    for p in processes:
        if p.poll() is None:
            p.wait()