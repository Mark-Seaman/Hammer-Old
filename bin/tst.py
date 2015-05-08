#!/usr/bin/env python

from glob import glob
from os import system
from os.path import join
from subprocess import Popen,PIPE
from sys import argv
from re import sub

from diff_tests import run_diff_checks, shell, lines, limit_lines



def process_status_test():
    '''   Make sure that there are not too many processes running   '''
    return limit_lines ('ps -e',10,250)


def pwd_test():
    '''   List the current directory   '''
    return shell('pwd')


def ls_test():
    '''   List files in the current directory   '''
    return shell('ls')


def source_lines_test():
    '''   Count the lines of source code in the tst.py file   '''
    return limit_lines ('cat bin/tst.py',70,80)


def like_test():
    '''   Test the like switch to approve the correct answer   '''
    system('''
        echo do not like this > test/dummy.correct
        tst like dummy > /dev/null
        ''')
    return ''
 

def output_test():
    '''   Display the output from the last test run   '''
    return shell('tst output cmd_add')



def main():
    '''Execute all tests for the tst command'''
    my_tests = {
        'like': like_test,
        'lines': source_lines_test,
        'ls': ls_test,
        # 'nose': nose_test_execution,
        'output': output_test,
        'ps': process_status_test,
        'pwd': pwd_test,
    }
    run_diff_checks('tst', argv, my_tests)

   

# Create a script that can be run from the tst
if __name__=='__main__':
    main()
