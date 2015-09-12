'''
Tests for code code
-------------------

Run all of the tests for the 'code' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines


def code_list_test():
    return shell('code list')


def code_show_test():
    return limit_lines('code show bin/code.py',150,180)


def code_complexity_test():
    return shell('code complexity')

