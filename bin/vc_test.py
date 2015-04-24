'''
Tests for vc code
-------------------

Run all of the tests for the 'vc' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join


def vc_add_test():
	system('vc add xxx')


def vc_delete_test():
	system('vc delete xxx')


def vc_edit_test():
	system('vc edit xxx')


def vc_list_test():
	system('vc list xxx')


def vc_show_test():
	system('vc show xxx')

