'''
Tests for extra code
-------------------

Run all of the tests for the 'extra' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def extra_outline_test():
    return shell('extra outline')


def extra_show_test():
    return shell('extra show')


def extra_checker():
    my_tests = {
        'extra-outline': extra_outline_test,
        'extra-show': extra_show_test,
    }
    run_diff_checks('extra', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    extra_checker()
