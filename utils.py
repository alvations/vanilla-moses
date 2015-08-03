#!/usr/bin/env python -*- coding: utf-8 -*-

import subprocess
import os

def parallelized_download(command, files, arguments="", max_processes=2):
    processes = set()
    for name in files:
        if os.path.exists(name):
            continue
        processes.add(subprocess.Popen([command, name]))
        if len(processes) >= max_processes:
            os.wait()
            processes.difference_update(
                [p for p in processes if p.poll() is not None])
    #Check if all the child processes were closed
    for p in processes:
        if p.poll() is None:
            p.wait()