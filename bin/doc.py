#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv


def doc_add(argv):
	'''	
	Create a new doc.
	'''
	print("New doc:"+argv[2])
	system('echo "Document %s" > docs/%s' % (argv[2],argv[2]))


def doc_delete(argv):
	'''	
	Delete the doc.
	'''
	print("rm docs/"+argv[2])
	system('rm docs/'+argv[2])


def doc_edit(argv):
	'''	
	Edit the content of a doc.
	'''
	print("doc:",argv[2])
	system('e docs/'+argv[2])


def doc_help():
	'''
	Show all the doc docs and their usage.
	'''
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
	'''
	List the parts of the doc source code.
	'''
	print("List the contents of this doc")
	for d in ('docs',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def doc_show(argv):
	'''	
	Show the content of a doc.
	'''
	print("doc:",argv[2])
	system('cat docs/%s' % argv[2])


def doc_doc(argv):
	'''
	Execute all of the doc specific docs
	'''
	if len(argv)>1:

		if argv[1]=='add':
			doc_add(argv)
			exit(0)

		if argv[1]=='delete':
			doc_delete(argv)
			exit(0)

		if argv[1]=='edit':
			doc_edit(argv)
			exit(0)

		if argv[1]=='list':
			doc_list(argv)
			exit(0)

		if argv[1]=='show':
			doc_show(argv)
			exit(0)

		if argv[1]=='commit':
			commit_doc(argv)
			exit(0)

		if argv[1]=='test':
			system('nosetests -v')
			exit(0)		

		print('No doc doc found, '+argv[1])
		
	doc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	doc_doc(argv)