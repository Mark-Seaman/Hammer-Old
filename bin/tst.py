#!/usr/bin/env python

from glob import glob
from os.path import join
from subprocess import Popen,PIPE
from sys import argv

from diff_tests import execute_command, shell, lines


def pwd_test():
    '''
    List the current directory
    '''
    return shell('pwd')


def ls_test():
    '''
    List files in the current directory
    '''
    return shell('ls')


def source_test():
    '''
    List the source files from several directories
    '''
    dirs = ['','bin','test']
    result = []
    for d in dirs:
        result += glob(join(d,'*.py'))
    return '\n'.join(result)+'\n'


def count_source_lines_test():
    '''
    Count the lines of source code in the tst.py file
    '''
    text = shell ('cat bin/tst.py')
    violation = lines(text,55,60)
    if violation:
        return violation+'\n'+text
    return text
    

my_tests = {
    'pwd': pwd_test,
    'ls': ls_test,
    'source': source_test,
    'lines': count_source_lines_test,
}


'''
Create a script that can be run from the tst
'''
if __name__=='__main__':
    execute_command(my_tests)
