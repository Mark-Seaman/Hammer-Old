'''
Tests for system code
-------------------

Run all of the tests for the 'system' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def system_add_test():
    return shell('system add xxx')


def system_delete_test():
    return shell('system delete xxx')


def system_edit_test():
    return shell('system edit xxx')


def system_list_test():
    return shell('echo system list xxx')


def system_show_test():
    return shell('echo system show xxx')


def system_checker():
    my_tests = {
        'system-add': system_add_test,
        'system-list': system_list_test,
        'system-delete': system_delete_test,
        'system-show': system_show_test,
    }
    run_diff_checks('system', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    system_checker()
