#!/usr/bin/env python

from os import system

from shell import shell, lines, limit_lines


def tst_modules_test():
    return shell ('tst modules')


def tst_functions_test():
    return shell ('tst functions')


def tst_cases_test():
    return shell('tst cases')


def tst_lines_test():
    return limit_lines ('cat bin/tst.py',200,370)


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
