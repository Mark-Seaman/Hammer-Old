'''
Tests for code code
-------------------

Run all of the tests for the 'code' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def code_add_test():
    return shell('echo code add xxx')


def code_delete_test():
    return shell('echo code delete xxx')


def code_edit_test():
    return shell('echo code edit xxx')


def code_list_test():
    return shell('code list')


def code_show_test():
    return shell('code show bin/code.py')


def code_complexity_test():
    return shell('code complexity')


def code_checker():
    my_tests = {
        'code-add': code_add_test,
        'code-list': code_list_test,
        'code-delete': code_delete_test,
        'code-show': code_show_test,
        'code-complexity': code_complexity_test,
    }
    run_diff_checks('code', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    code_checker()
