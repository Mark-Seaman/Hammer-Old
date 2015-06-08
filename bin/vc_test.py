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
    '''Test the commits'''
    return shell('vc')


def vc_delete_test():
    '''Test removing files from version control'''
    return shell('echo Can not test this command')


def vc_help_test():
    '''Test the version command help'''
    return shell('vc help')


def vc_show_test():
    '''Test showing source code changes'''
    differences =  shell('vc show').split('\n')
    if len(differences)>100:
        return  'More than 100 differences in the vc show output'


def vc_status_test():
    '''Test the git status command'''
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
