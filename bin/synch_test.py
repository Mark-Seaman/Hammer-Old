'''
Tests for synch code
-------------------

Run all of the tests for the 'synch' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines


def clean_up():
    system('rm -rf test-xxx')
    

def synch_bin_test():
    return limit_lines('synch bin', 2, 10)


def synch_copy_test():
    x = limit_lines('synch copy test test-xxx',130,300)
    clean_up()
    return x


def synch_preview_test():
	return limit_lines('synch preview test test-xxx',130, 300)


def synch_mirror_test():
    shell('synch mirror test test-xxx')
    x = limit_lines('synch mirror test test-xxx', 6, 6)
    clean_up()
    return x


def synch_sync_test():
    x = limit_lines('synch sync test test-xxx', 120, 300)
    clean_up()
    return x


def synch_help_test():
    return shell('synch help')
