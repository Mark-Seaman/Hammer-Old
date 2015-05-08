'''
Tests for vc code
-------------------

Run all of the tests for the 'vc' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join
from sys import argv

from diff_tests import run_diff_checks, shell, lines, limit_lines


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


def vc_test():
    '''   Test the vc command set   '''
    return shell('vc test')


def main():
    '''Execute all the desired diff tests'''
    my_tests = {
        'vc': vc_test,
    }
    run_diff_checks('vc', argv, my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    print('main()')
