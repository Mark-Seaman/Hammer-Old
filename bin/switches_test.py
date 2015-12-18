'''
Tests for switches code
-------------------

Run all of the tests for the 'switches' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines



def switches_list_test():
    return shell('switches list')


def switches_path_test():
    return shell('switches path') 


def switches_load_test():
    return shell('switches load && switches list')
