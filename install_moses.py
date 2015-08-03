#!/usr/bin/env python -*- coding: utf-8 -*-

import os, subprocess
import platform

from multiprocessing import Process

moses_install_url = 'http://www.statmt.org/moses/?n=Development.GetStarted'
moses_github_repo = 'https://github.com/moses-smt/mosesdecoder.git'    
moses_training_tools = 'http://www.statmt.org/moses/RELEASE-3.0/binaries/linux-64bit/training-tools/'
moses_sample_model = 'http://www.statmt.org/moses/download/sample-models.tgz'
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
                            #stdout=open(os.devnull,"wb"), 
                            stderr=subprocess.STDOUT, executable="/bin/bash")
    proc.wait()
    return proc


def download_moses_training_tools():
    if os.path.exists('moses-training-tools'): return;
    run_command('wget -r --no-parent --reject "index.html*" %s' % 
                moses_training_tools)
    path_to_training_tools = str('www.statmt.org/moses/RELEASE-3.0/binaries/'
                                'linux-64bit/training-tools/')
    run_command('mv '+ path_to_training_tools + ' moses-training-tools')
    run_command('rm -rf www.statmt.org/')
    
def download_moses_github_repo():
    if os.path.exists('mosesdecoder'): return;
    run_command('git clone '+moses_github_repo)
    
    
def install_moses():
    os.chdir('mosesdecoder/')
    if os.path.exists('bin/moses'): return;
    run_command('./bjam -j4 -max-kenlm-order=20')

def check_installed_moses():
    os.chdir(os.path.expanduser("~")+ '/mosesdecoder')
    if not os.path.exists('sample-models.tgz'):
        run_command('wget '+ moses_sample_model)
        run_command('tar xzf sample-models.tgz')
    os.chdir('sample-models')
    proc = run_command(str('~/mosesdecoder/bin/moses -f '
                           'phrase-model/moses.ini < phrase-model/in > out'))
    print(open('out', 'r').read().strip())

##############################################################################

# Checks whether it's 64-bit Ubuntu.
not_64bit_ubuntu_error_msg = str("This only works on 64-bit Ubuntu...\n" 
                                  "For other OS See %s" % moses_install_url)

# Change to home diectory
homedir = os.path.expanduser("~")
os.chdir(homedir)

# Download repo and training tools
print('Downloading Moses repo and tools...')
repo_thread = Process(target = download_moses_github_repo)
tool_thread = Process(target = download_moses_training_tools)
repo_thread.start(); tool_thread.start()
repo_thread.join(); tool_thread.join()

# Install moses
print('Installing Moses...')
install_moses()

# Check installed moses.
print('Checking installed Moses...')
check_installed_moses()