#!/usr/bin/env python

from glob import glob
from os import system
from os.path import join
from subprocess import Popen,PIPE
from sys import argv
from re import sub

from shell import shell, lines, limit_lines
from tst import run_diff_checks


def tst_modules_test():
    return shell ('tst modules')


def tst_functions_test():
    return shell ('tst functions')


def tst_cases_test():
    return shell('tst cases')


def tst_lines_test():
    return limit_lines ('cat bin/tst.py',200,350)


def tst_like_test():
    system('''
        echo do not like this > test/dummy.correct
        tst like dummy > /dev/null
        ''')
    return ''

 
def tst_list_tests():
     '''Make a list of all tests to run'''
     return shell('tst list')

def tst_list_names():
     '''Make a list of all tests to run'''
     return shell('tst list')


def tst_output_test():
    '''   Display the output from the last test run   '''
    return shell('tst output cmd_add')


def tst_help_test():
    return shell('tst help')


def tst_checker():
    my_tests = {
        'tst-modules': tst_modules_test,
        'tst-functions': tst_functions_test,
        'tst-cases': tst_cases_test,
        'tst-like': tst_like_test,
        'tst-lines': tst_lines_test,
        'tst-names': tst_list_names,
        'tst-list': tst_list_tests,
        'tst-help': tst_help_test,
        'tst-output': tst_output_test,
    }
    run_diff_checks('tst', my_tests)

   

# Create a script that can be run from the tst
if __name__=='__main__':
    tst_checker()
