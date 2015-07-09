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
    return shell('book build')


def book_status_test():
    return shell('book status')


def book_help_test():
    return shell('book help')

def book_headlines_test():
    return shell('book headlines')


def book_list_test():
    return shell('book list')


def book_words_test():
    return shell('book words')
    

def book_text():
    '''Get the text for Chapter 1'''
    return shell('book text Teamwork')


def book_checker():
    '''Execute all the desired diff tests'''
    my_tests = {
        'book-status': book_status_test,
        'book-build': book_build_test,
        'book-headlines': book_headlines_test,
        'book-help': book_help_test,
        'book-list': book_list_test,
        'book-text': book_text,
        'book-words': book_words_test,
    }
    run_diff_checks('book', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    book_checker()