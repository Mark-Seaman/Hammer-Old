#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

def doc_path(doc):
	'''Return the path name that corresponds to this document.'''
	return join(environ['pd'],doc)


def doc_add(argv):
	'''	Create a new doc.'''
	print("New doc:"+argv[2])
	system('echo "Document %s" > docs/%s' % (argv[2],argv[2]))


def doc_delete(argv):
	'''	Delete the doc.'''
	print("rm docs/"+argv[2])
	system('rm docs/'+argv[2])


def doc_edit(argv):
	'''	Edit the content of a doc.'''
	print("doc:",argv[2])
	system('e docs/'+argv[2])


def doc_help():
	'''Show all the doc docs and their usage.'''
	print('''
    usage: cmd doc [args]

    doc:

        add     [file] -- Add a new doc
        delete  [file] -- Delete a doc
        edit    [file] -- Edit the doc
        list    [file] -- List all docs
        show    [file] -- Show a doc
      
			''')


def doc_list(argv):
	'''List the parts of the doc source code.'''
	print("List the contents of this doc")
	for d in ('docs',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def doc_show(argv):
	'''	Show the content of a doc.'''
	print("doc:",argv[2])
	system('cat docs/%s' % argv[2])


def doc_command(argv):
	'''Execute all of the doc specific docs'''
	if len(argv)>1:

		if argv[1]=='add':
			doc_add(argv)

		elif argv[1]=='delete':
			doc_delete(argv)

		elif argv[1]=='edit':
			doc_edit(argv)

		elif argv[1]=='list':
			doc_list(argv)

		elif argv[1]=='show':
			doc_show(argv)

		elif argv[1]=='commit':
			commit_doc(argv)

		elif argv[1]=='test':
			system('echo nosetests -v')

		else:
			print('No doc doc found, '+argv[1])
	else:
		doc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	doc_command(argv)