'''
Tests for vc code
-------------------

Run all of the tests for the 'vc' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join
from sys import argv

from shell import  shell, lines, limit_lines


def vc_changes_test():
    '''Test the commits'''
    return shell('vc changes')


def vc_help_test():
    '''Test the version command help'''
    return shell('vc help')


def vc_status_test():
    '''Test the git status command'''
    return shell('vc status')

