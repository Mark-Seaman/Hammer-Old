'''
Tests for lan code
-------------------

Run all of the tests for the 'lan' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def lan_list_test():
    return shell('lan list')
    

def lan_checker():
    my_tests = {
        'lan-list': lan_list_test,
    }
    run_diff_checks('lan', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    lan_checker()
