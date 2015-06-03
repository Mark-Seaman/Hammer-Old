'''
Tests for code code
-------------------

Run all of the tests for the 'code' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def code_list_test():
    return shell('code list')


def code_show_test():
    return shell('code show bin/code.py')


def code_complexity_test():
    return shell('code complexity')


def code_functions_test():
    return shell('code functions')


def code_checker():
    my_tests = {
        'code-list': code_list_test,
        'code-show': code_show_test,
        'code-complexity': code_complexity_test,
        'code-functions': code_functions_test,
    }
    run_diff_checks('code', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    code_checker()
