#!/usr/bin/env python -*- coding: utf-8 -*-

import os
from subprocess import Popen
from os.path import expanduser
from multiprocessing import Process

moses_install_url = 'http://www.statmt.org/moses/?n=Development.GetStarted'
moses_github_repo = 'https://github.com/moses-smt/mosesdecoder.git'    
moses_training_tools = 'http://www.statmt.org/moses/RELEASE-3.0/binaries/linux-64bit/training-tools/'

##############################################################################

def check_is_linux(distro, architecture, 
                   err_msg="SNL: Something-else, Not Linux!!"):
    try:
        this_os = Popen('lsb_release -d').read()
        this_arch = Popen('uname -a').read()
        
        assert distro in this_os and architecture in this_arch, err_msg
    except:
        print(err_msg)

def check_is_64bit_ubuntu(err_msg):
    check_is_linux('Ubuntu', 'x86_64', err_msg)
    

def download_moses_training_tools():
    if not os.path.exists('moses-training-tools'): return;
    Popen('wget -r --no-parent '+ moses_training_tools)
    Popen.wait()
    Popen('mv training-tools moses-training-tools')

def download_moses_github_repo():
    if not os.path.exists('mosesdecoder'): return;
    Popen('git clone '+moses_github_repo)
    
    
def install_moses():
    os.chdir('mosesdecoder/')
    if not os.path.exists('bin/moses'): return;
    Popen('./bjam -j4 -max-kenlm-order 20')
    Popen.wait()
    
    
##############################################################################

# Checks whether it's 64-bit Ubuntu. 
not_64bit_ubuntu_error_msg = str("This only works on 64-bit Ubuntu...\n" 
                                  "For other OS See %s" % moses_install_url)
check_is_64bit_ubuntu(not_64bit_ubuntu_error_msg)

# Change to home diectory
homedir = expanduser("~")
os.chdir(homedir)

# Download repo and training tools
repo_thread = Process(target = download_moses_github_repo).start()
tools_thread = Process(target = download_moses_training_tools).start()
repo_thread.join()
tools_thread.join()

# Install moses
install_moses()


