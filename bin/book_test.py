'''
Book Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists
from sys import argv

from tst import run_diff_checks, shell, lines, limit_lines


def book_changes_test():
    '''Make sure there are no uncommitted changes pending'''
    return shell('book changes')

def book_assemble_test():
    '''Test the assembly of a book from its parts'''
    return shell('book assemble')


def book_files_test():
    '''Show a list of all the source files in the book'''
    return shell('book book_files')


def book_help_test():
    '''Show help for book script'''
    return shell('book help')


def book_list_test():
    '''List all of the existing documents '''
    #return limit_lines('book list', 4, 8)
    return shell('book list')


def book_outline_test():
    '''Create a book outline'''
    return shell('book outline')


def book_checker():
    '''Execute all the desired diff tests'''
    my_tests = {
    'book-changes': book_changes_test,
        'book-assemble': book_assemble_test,
        'book-files': book_files_test,
        'book-help': book_help_test,
        'book-list': book_list_test,
        'book-outline': book_outline_test,

    }
    run_diff_checks('book', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    book_checker()