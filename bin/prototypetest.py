'''
Tests for prototype code
-------------------

Run all of the tests for the 'prototype' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def prototype_add_test():
    return shell('echo prototype add xxx')


def prototype_delete_test():
    return shell('echo prototype delete xxx')


def prototype_edit_test():
    return shell('echo prototype edit xxx')


def prototype_list_test():
    return shell('echo prototype list xxx')


def prototype_show_test():
    return shell('echo prototype show xxx')


def prototype_checker():
    my_tests = {
        'prototype-add': prototype_add_test,
        'prototype-list': prototype_list_test,
        'prototype-delete': prototype_delete_test,
        'prototype-show': prototype_show_test,
    }
    run_diff_checks('prototype', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    prototype_checker()
