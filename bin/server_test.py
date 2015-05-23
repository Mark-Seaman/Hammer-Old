'''
Tests for server code
-------------------

Run all of the tests for the 'server' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def server_host_test():
    return shell('server host')


def server_status_test():
    return limit_lines('server status', 10,20)


def server_changes_test():
    return shell('server changes')


def server_list_test():
    return shell('echo server list xxx')


def server_show_test():
    return shell('echo server show xxx')


def server_help_test():
    return shell('server help')


def server_checker():
    my_tests = {
        'server-host': server_host_test,
        'server-status': server_status_test,
        'server-changes': server_changes_test,
        'server-show': server_show_test,
        'server-help': server_help_test,
    }
    run_diff_checks('server', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    server_checker()
