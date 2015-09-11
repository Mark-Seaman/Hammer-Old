'''
Document Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists
from sys import argv

from shell import shell, lines, limit_lines
from tst import run_diff_checks


def doc_add_test():
	return shell('doc add xxx_sample_document') + shell('doc delete xxx_sample_document')


def doc_status_test():
    return limit_lines('doc status', 0, 100)


def doc_list_test():
	return limit_lines('doc list', 10, 25)


def doc_path_test():
	return shell('doc path test_this') + shell('doc path test_that')


def doc_show_test():
	text = limit_lines('doc show', 99, 99)
	return text


def doc_checker():
	'''Execute all the desired diff tests'''
	my_tests = {
        'doc-add': doc_add_test,
        'doc-status': doc_status_test,
        'doc-list': doc_list_test,
        'doc-path': doc_path_test,
        'doc-show': doc_show_test,
    }
	run_diff_checks('doc', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    doc_checker()