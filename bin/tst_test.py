#!/usr/bin/env python

from glob import glob
from os import system
from os.path import join
from subprocess import Popen,PIPE
from sys import argv
from re import sub

from tst import run_diff_checks, shell, lines, limit_lines


def lines_test():
    '''   Count the lines of source code in the tst.py file   '''
    return limit_lines ('cat bin/tst.py',300,320)


def like_test():
    '''   Test the like switch to approve the correct answer   '''
    system('''
        echo do not like this > test/dummy.correct
        tst like dummy > /dev/null
        ''')
    return ''

 
# def list_tests():
#     '''Make a list of all tests to run'''
#     return shell('tst list')


def output_test():
    '''   Display the output from the last test run   '''
    return shell('tst output cmd_add')


def help_test():
    return shell('tst help')


def tst_checker():
    '''Execute all tests for the tst command'''
    my_tests = {
        'tst-like': like_test,
        'tst-lines': lines_test,
        #'tst-list': list_tests,
        'tst-help': help_test,
        'tst-output': output_test,
    }
    run_diff_checks('tst', my_tests)

   

# Create a script that can be run from the tst
if __name__=='__main__':
    tst_checker()
