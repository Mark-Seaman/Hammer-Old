'''
Book Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists
from sys import argv

from tst import run_diff_checks, shell, lines, limit_lines


def book_build_test():
    '''Test the assembly of a book from its parts'''
    return shell('book build')


def book_changes_test():
    '''Make sure there are no uncommitted changes pending'''
    return shell('book changes')


def book_help_test():
    '''Show help for book script'''
    return shell('book help')


def book_list_test():
    '''List all of the existing documents '''
    #return limit_lines('book list', 4, 8)
    return shell('book list')


def book_outline_test():
    '''Create a book outline'''
    return limit_lines('book outline', 14,15)


def book_words_test():
    '''Test the number of words in the book'''
    return shell('book words')


def book_text():
    '''Get the text for Chapter 1'''
    return shell('book text Culture')


def book_checker():
    '''Execute all the desired diff tests'''
    my_tests = {
        'book-changes': book_changes_test,
        'book-build': book_build_test,
        'book-help': book_help_test,
        'book-list': book_list_test,
        'book-outline': book_outline_test,
        'book-text': book_text,
        'book-words': book_words_test,
    }
    run_diff_checks('book', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    book_checker()