'''
Book Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists
from sys import argv

from tst import run_diff_checks, shell, lines, limit_lines


def book_list_test():
    '''List all of the existing documents '''
    #return limit_lines('book list', 4, 8)
    return shell('book list')


def book_assemble_test():
    '''Test the assembly of a book from its parts'''
    return shell('book assemble')


def book_checker():
    '''Execute all the desired diff tests'''
    my_tests = {
        'book-list': book_list_test,
        'book-assemble': book_assemble_test,
    }
    run_diff_checks('book', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    book_checker()