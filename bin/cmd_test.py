'''
Command Tests
---------------

Run all of the tests for the 'cmd' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from diff_tests import shell


def cmd_add_test():
    print(shell('cmd add xxx'))
    print(shell('cmd show xxx'))
    print(shell('cmd delete xxx'))


def cmd_list_test():
	shell('cmd list xxx')


def cmd_python_pip_test():
	shell('pip list')

