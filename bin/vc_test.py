'''
Tests for vc code
-------------------

Run all of the tests for the 'vc' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join
from sys import argv

from shell import  shell, lines, limit_lines


def vc_commit_test():
    '''Test the commits'''
    system('vc > /dev/null')
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

