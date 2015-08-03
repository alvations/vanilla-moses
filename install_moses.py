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
    

def run_command(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdin=None, 
                            stdout=open(os.devnull,"wb"), 
                            stderr=subprocess.STDOUT, executable="/bin/bash")
    return proc


def download_moses_training_tools():
    if os.path.exists('moses-training-tools'): return;
    proc = run_command('wget -r --no-parent --reject "index.html*" %s' % 
                       moses_training_tools)
    proc.wait()
    path_to_training_tools = str('www.statmt.org/moses/RELEASE-3.0/binaries/'
                                'linux-64bit/training-tools/')
    proc = run_command('mv '+ path_to_training_tools + ' moses-training-tools')

def download_moses_github_repo():
    if os.path.exists('mosesdecoder'): return;
    proc = run_command('git clone '+moses_github_repo)
    proc.wait()
    
    
def install_moses():
    os.chdir('mosesdecoder/')
    if os.path.exists('bin/moses'): return;
    proc = run_command('./bjam -j4 -max-kenlm-order 20')
    proc.wait()
    
def install_dependencies():
    dependencies = str('g++ git subversion automake libtool zlib1g-dev '
                       'libboost-all-dev libbz2-dev liblzma-dev '
                       'python-dev graphviz libgoogle-perftools-dev')
    proc = run_command('apt-get install '+dependencies)
    proc.wait()
    
##############################################################################

# Checks whether it's 64-bit Ubuntu.
not_64bit_ubuntu_error_msg = str("This only works on 64-bit Ubuntu...\n" 
                                  "For other OS See %s" % moses_install_url)

# Change to home diectory
homedir = os.path.expanduser("~")
os.chdir(homedir)

# Install Moses dependencies.
install_dependencies()

# Download repo and training tools
repo_thread = Process(target = download_moses_github_repo)
tool_thread = Process(target = download_moses_training_tools).start()
repo_thread.start(); tool_thread.start()
repo_thread.join(); tool_thread.join()

# Install moses
install_moses()
