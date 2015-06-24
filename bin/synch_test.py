'''
Tests for synch code
-------------------

Run all of the tests for the 'synch' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def clean_up():
    system('rm -rf test-xxx')
    

def synch_copy_test():
    x = limit_lines('synch copy test test-xxx')
    clean_up()
    return x


def synch_preview_test():
	return limit_lines('synch preview test test-xxx',130, 140)


def synch_mirror_test():
    shell('synch mirror test test-xxx')
    x = limit_lines('synch mirror test test-xxx', 6, 6)
    clean_up()
    return x


def synch_sync_test():
    x = limit_lines('synch sync test test-xxx', 120, 150)
    clean_up()
    return x


def synch_help_test():
    return shell('synch help')


def synch_checker():
    my_tests = {
        'synch-copy': synch_copy_test,
        'synch-preview': synch_preview_test,
        'synch-mirror': synch_mirror_test,
        'synch-sync': synch_sync_test,
        'synch-help': synch_help_test,
    }
    run_diff_checks('synch', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    synch_checker()