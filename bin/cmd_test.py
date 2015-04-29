'''
Command Tests
---------------

Run all of the tests for the 'cmd' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from diff_tests import shell


def cmd_add_test():
    return shell('cmd add xxx') + shell('cmd show xxx') + shell('cmd delete xxx')


def cmd_list_test():
	return shell('cmd list xxx')


def cmd_python_pip_test():
	return shell('pip list')

