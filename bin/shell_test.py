'''
Tests for shell code
-------------------

Run all of the tests for the 'shell' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import on_internet, shell


def shell_list_test():
    from shell import shell
    return shell('shell list')


def shell_path_test():
    from shell import shell
    return shell('shell path') + '\n' + shell('shell path xxx')


def shell_show_test():
    from shell import shell
    return shell('shell show')


def shell_internet_test():
    if on_internet():
        return shell('git pull')
