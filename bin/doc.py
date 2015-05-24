#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join, exists
from sys import argv

from doc_test import doc_checker


def doc_path(doc):
	'''Return the path name that corresponds to this document.'''
	return join(environ['pd'],doc)


def doc_add(argv):
	'''	Create a new doc.'''
	d = doc_path(argv[2])
	print("New doc:"+d)
	system('echo "Document %s" > %s' % (d,d))


def doc_delete(argv):
	'''	Delete the doc.'''
	d = doc_path(argv[2])
	if not exists(d):
		print('doc delete: no file found, '+d)
	else:
		print('doc delete: '+d)
		system('rm '+d)


def doc_edit(argv):
	'''	Edit the content of a doc.'''
	d = doc_path(argv[2])
	print("edit:",d)
	system('e '+d)


def doc_help():
	'''Show all the doc docs and their usage.'''
	print('''
    usage: cmd doc [args]

    doc:

        add     [file] -- Add a new doc
        delete  [file] -- Delete a doc
        edit    [file] -- Edit the doc
        list    [file] -- List all docs
        path    [file] -- Show path to document
        show    [file] -- Show a doc
        text           -- Show markdown for all docs
      
			''')


def doc_path(filename=''):
	return join(environ['mb'], filename)


def doc_list(argv):
	'''List the parts of the doc source code.'''
	print("List the contents of this doc")
	for d in ('docs',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def doc_show(docs):
	'''	Show the content of a doc.'''
	if docs:
		for d in docs:
			d = doc_path(d)
			print("doc:",d)
			system('cat '+d)
	else:
		d = doc_path('')
		for f in listdir(d):
			print("# doc:",d+f)	
			system('cat '+d+f)
	

def doc_command(argv):
	'''Execute all of the doc specific docs'''
	if len(argv)>1:

		if argv[1]=='add':
			doc_add(argv)

		elif argv[1]=='commit':
			commit_doc(argv)

		elif argv[1]=='delete':
			doc_delete(argv)

		elif argv[1]=='edit':
			doc_edit(argv)

		elif argv[1]=='list':
			doc_list(argv)

		elif argv[1]=='path':
			print('path:'+doc_path(argv[2]))

		elif argv[1]=='show':
			doc_show(argv[2:])

		elif argv[1]=='test':
			doc_checker()

		else:
			print('No doc doc found, '+argv[1])
	else:
		doc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	doc_command(argv)