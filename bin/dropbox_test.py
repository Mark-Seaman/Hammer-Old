'''
Tests for dropbox code
-------------------

Run all of the tests for the 'dropbox' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def dropbox_add_test():
    return shell('echo dropbox add xxx')


def dropbox_delete_test():
    return shell('echo dropbox delete xxx')


def dropbox_edit_test():
    return shell('echo dropbox edit xxx')


def dropbox_list_test():
    return shell('echo dropbox list xxx')


def dropbox_show_test():
    return shell('echo dropbox show xxx')


def dropbox_checker():
    my_tests = {
        'dropbox-add': dropbox_add_test,
        'dropbox-list': dropbox_list_test,
        'dropbox-delete': dropbox_delete_test,
        'dropbox-show': dropbox_show_test,
    }
    run_diff_checks('dropbox', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    dropbox_checker()
