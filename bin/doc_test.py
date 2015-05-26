'''
Document Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists
from sys import argv

from tst import run_diff_checks, shell, lines, limit_lines


def doc_add_test():
	return shell('doc add xxx_sample_document') + shell('doc delete xxx_sample_document')


def doc_list_test():
	return limit_lines('doc list', 20, 25)


def doc_path_test():
	return shell('doc path test_this') + shell('doc path test_that')


def doc_show_test():
	text = limit_lines('doc show Leverage/Book.index', 6, 6)
	text += limit_lines('doc show Leverage/Chapters.index', 14, 14) 
	return text


def doc_checker():
	'''Execute all the desired diff tests'''
	my_tests = {
        'doc-add': doc_add_test,
        'doc-list': doc_list_test,
        'doc-path': doc_path_test,
        'doc-show': doc_show_test,
    }
	run_diff_checks('doc', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    doc_checker()