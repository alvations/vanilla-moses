#!/usr/bin/env python -*- coding: utf-8 -*-

import subprocess
import os

def file_from_url_exists(url):
    filename = url.rpartition('/')[2]
    return os.path.exists(filename)

def parallelized_commandline(command, files, arguments="",
                             max_processes=2, file_exists=os.path.exists):
    processes = set()
    for name in files:
        if file_exists(name):
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
            
def parallelized_download(command, urls):
    paralleilized_commandline(command, urls, file_exists=file_from_url_exists)