'''
Tests for app code
-------------------

Run all of the tests for the 'app' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines


def app_list_test():
    return shell('app list')


def app_path_test():
    return shell('app path') + '\n' + shell('app path xxx')


def app_show_test():
    return shell('app show app.py')


def app_syncdb_test():
    return shell('app syncdb')
