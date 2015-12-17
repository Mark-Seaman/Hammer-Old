'''
Tests for server code
-------------------

Run all of the tests for the 'server' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines


def server_host_test():
    return shell('server host')


def server_status_test():
    return limit_lines('server status', 10,20)


def server_changes_test():
    return shell('server changes')


def server_help_test():
    return shell('server help')
