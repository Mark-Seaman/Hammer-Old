'''
Document Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists

from diff_tests import lines, shell


def doc_add_test():
	print(shell('doc add xxx_sample_document'))
	assert(exists(join(environ['pd'],'xxx_sample_document')))


def doc_delete_test():
	print(shell('doc delete xxx_sample_document'))
	assert(not exists(join(environ['pd'],'xxx_sample_document')))


def doc_list_test():
	doc_list = shell('doc list')
	violation = lines(doc_list, 4, 6)
	print('Doc list: %s' % violation)
	assert(not violation)


def doc_show_test():
	text = shell('doc show todo')
	print(text)
	x = lines(text,30,37)
	print('lines: %s' % x)
	assert(not x)

