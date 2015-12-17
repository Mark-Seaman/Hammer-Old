'''
Command Tests
---------------

Run all of the tests for the 'cmd' objects.  Output the test results.

'''

from glob import glob
from os import listdir, environ, system
from os.path import join
from sys import argv

from shell import shell, lines, limit_lines


def cmd_show_test():
    return(shell('cmd show cmd') + '\n' + shell('cmd show xxx'))


def cmd_list_test():
    return(shell('cmd list'))


def cmd_source_test():
    files = glob('bin/*.py')
    return '\n'.join(sorted(files))
