'''
Tests for synch code
-------------------

Run all of the tests for the 'synch' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def synch_add_test():
	return shell('echo synch add xxx')


def synch_delete_test():
	return shell('echo synch delete xxx')


def synch_edit_test():
	return shell('echo synch edit xxx')


def synch_list_test():
	return shell('echo synch list xxx')


def synch_show_test():
	return shell('echo synch show xxx')


def synch_checker():
    my_tests = {
        'synch-add': synch_add_test,
        'synch-list': synch_list_test,
        'synch-delete': synch_delete_test,
        'synch-show': synch_show_test,
    }
    run_diff_checks('synch', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    synch_checker()