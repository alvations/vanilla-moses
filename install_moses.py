#!/usr/bin/env python -*- coding: utf-8 -*-

import os, subprocess
import platform

from multiprocessing import Process

moses_install_url = 'http://www.statmt.org/moses/?n=Development.GetStarted'
moses_github_repo = 'https://github.com/moses-smt/mosesdecoder.git'    
moses_training_tools = 'http://www.statmt.org/moses/RELEASE-3.0/binaries/linux-64bit/training-tools/'

##############################################################################

def is_linux(distro, architecture):
    if not platform.system() == 'Linux':
        return False
    if platform.linux_distribution()[0].lower() != distro:
        return False
    return platform.processor() == architecture
    
    
def is_64bit_ubuntu():
    return is_linux('ubuntu', 'x86_64')
    

def download_moses_training_tools():
    if not os.path.exists('moses-training-tools'): return;
    subprocess.Popen('wget -r --no-parent '+ moses_training_tools)
    subprocess.Popen.wait()
    subprocess.Popen('mv training-tools moses-training-tools')

def download_moses_github_repo():
    if not os.path.exists('mosesdecoder'): return;
    subprocess.Popen('git clone '+moses_github_repo)
    subprocess.Popen.wait()
    
    
def install_moses():
    os.chdir('mosesdecoder/')
    if not os.path.exists('bin/moses'): return;
    subprocess.Popen('./bjam -j4 -max-kenlm-order 20')
    subprocess.Popen.wait()
    
    
##############################################################################

# Checks whether it's 64-bit Ubuntu.
not_64bit_ubuntu_error_msg = str("This only works on 64-bit Ubuntu...\n" 
                                  "For other OS See %s" % moses_install_url)

# Change to home diectory
homedir = os.path.expanduser("~")
os.chdir(homedir)

# Download repo and training tools
Process(target = download_moses_github_repo).start()
Process(target = download_moses_training_tools).start()

# Install moses
#install_moses()
