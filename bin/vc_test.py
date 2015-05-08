'''
Tests for vc code
-------------------

Run all of the tests for the 'vc' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join
from sys import argv

from tst import run_diff_checks, shell, lines, limit_lines


def vc_commit_test():
	return shell('echo Can not test this command')

def vc_delete_test():
    return shell('echo Can not test this command')


def vc_help_test():
    return shell('vc help')


def vc_show_test():
    return shell('echo Can not test this command')


def vc_status_test():
	return shell('vc status')


def vc_checker():
    '''   Test the vc command set   '''
    my_tests = {
        'vc-commit': vc_commit_test,
        'vc-delete': vc_delete_test,
        'vc-help': vc_help_test,
        'vc-show': vc_show_test,
        'vc-status': vc_status_test,
    }
    run_diff_checks('vc', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    print(vc_checker())
