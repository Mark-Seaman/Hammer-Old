'''
Tests for code code
-------------------

Run all of the tests for the 'code' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines
from tst import run_diff_checks


def code_list_test():
    return shell('code list')


def code_show_test():
    return limit_lines('code show bin/code.py',177,180)


def code_complexity_test():
    return shell('code complexity')


def code_checker():
    my_tests = {
        'code-list': code_list_test,
        'code-show': code_show_test,
        'code-complexity': code_complexity_test,
    }
    run_diff_checks('code', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    code_checker()
