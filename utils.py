#!/usr/bin/env python -*- coding: utf-8 -*-

import os, subprocess
import platform
from multiprocessing import Process

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
            
def parallelized_download(command, urls, arguments="", max_processes=2):
    parallelized_commandline(command, urls, arguments=arguments, 
                             max_processes=max_processes, 
                             file_exists=file_from_url_exists) 


def is_linux(distro, architecture):
    if not platform.system() == 'Linux':
        return False
    if platform.linux_distribution()[0].lower() != distro:
        return False
    return platform.processor() == architecture
    
    
def is_64bit_ubuntu():
    return is_linux('ubuntu', 'x86_64')
    

def run_command(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdin=None, 
                            #stdout=open(os.devnull,"wb"), 
                            stderr=subprocess.STDOUT, executable="/bin/bash")
    proc.wait()
    return proc

def parallized_run_command(cmds, max_processes=2):
    processes = set()
    for cmd in cmds:
        proc = subprocess.Popen(cmd, shell=True, stdin=None, 
                                stderr=subprocess.STDOUT, executable="/bin/bash")
        processes.add(proc)
        if len(processes) >= max_processes:
            os.wait()
            processes.difference_update(
                [p for p in processes if p.poll() is not None])
    #Check if all the child processes were closed
    for p in processes:
        if p.poll() is None:
            p.wait()