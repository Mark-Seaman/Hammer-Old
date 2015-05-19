'''
Tests for synch code
-------------------

Run all of the tests for the 'synch' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def synch_copy_test():
    x = shell('synch copy test test-xxx')
    system('rm -rf test-xxx')
    #return x


def synch_preview_test():
	return shell('echo synch preview xxx yyy')


def synch_mirror_test():
	return shell('echo synch mirror xxx yyy')


def synch_sync_test():
	return shell('echo synch sync xxx yyy')


def synch_checker():
    my_tests = {
        'synch-copy': synch_copy_test,
        'synch-preview': synch_preview_test,
        'synch-mirror': synch_mirror_test,
        'synch-sync': synch_sync_test,
    }
    run_diff_checks('synch', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    synch_checker()