'''
Tests for vc code
-------------------

Run all of the tests for the 'vc' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join
from sys import argv

from diff_tests import execute_command, shell, lines, limit_lines


def vc_add_test():
	pass

def vc_delete_test():
	pass


def vc_edit_test():
	pass


def vc_status_test():
	return shell('vc status')


def vc_show_test():
	pass



'''
Create a test that can be run from the shell
'''
if __name__=='__main__':

    my_tests = {
        'vc': vc_status_test,
    }

    execute_command(argv, my_tests)