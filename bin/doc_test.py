'''
Document Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists
from sys import argv

from shell import shell, lines, limit_lines


def doc_add_test():
	return shell('doc add xxx_sample_document') + shell('doc delete xxx_sample_document')


def doc_status_test():
    return limit_lines('doc status', 0, 100)


def doc_list_test():
	return limit_lines('doc list', 590, 600)


def doc_path_test():
	return shell('doc path test_this') + shell('doc path test_that')


def doc_show_test():
	text = limit_lines('doc show', 99, 99)
	return text

