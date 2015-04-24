'''
Document Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join, exists


def doc_add_test():
	system('doc add xxx_sample_document')
	path = join(environ['pd'],'xxx_sample_document')
	print(path)
	assert(exists(path))


def doc_delete_test():
	system('doc delete xxx_sample_document')
	path = join(environ['pd'],'xxx_sample_document')
	assert(not exists(path))


def doc_edit_test():
	path = join(environ['pd'],'xxx_sample_document')
	assert(not exists(path))


def doc_list_test():
	system('doc list')


def doc_show_test():
	system('doc show todo')

