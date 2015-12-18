'''
Tests for synch code
-------------------

Run all of the tests for the 'synch' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines


def clean_up():
    system('rm -rf bin-xxx')
    

def synch_mirror_test():
    shell('synch mirror bin bin-xxx')
    x = limit_lines('synch mirror bin bin-xxx', 6, 6)
    clean_up()
    return x


def synch_sync_test():
    x = limit_lines('synch sync bin bin-xxx', 120, 300)
    clean_up()
    return x


def synch_help_test():
    return shell('synch help')
