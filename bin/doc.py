#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv


def assemble_doc_parts():
	'''
	Put together a markdown file from the individual parts
	'''
	print('Assemble: Index.md')
	parts = ('doc/Cover', 'doc/Abstract', 'doc/Intro', 'doc/Outline', 
		'chapters/Part1', 'chapters/Part2', 'chapters/Part3', 'chapters/Part4',
		'chapters/Part5', 'doc/10Ways')
	with open('docs/doc/doc.md','w') as output_file:
		for p in parts:
			output_file.write('\n\n---\n\n# '+p+'\n\n')
			path = 'docs/'+p+'.md'
			print('Build '+path+'  ...')
			text = open(path).read()	
			#print(text)
			output_file.write(text)


def commit_command(argv):
	'''
	Form the shell script for the commit command.
	'''
	comment = commit_comment(argv)
	command = '''#!/bin/bash
	# Commit all changes 

	cd $p
	git add -A .
	git commit -m"%s" 
	''' % comment
	print("Commit all changes from the doc project")
	system(command)


def commit_comment(argv):
	'''
	Select the comment to tag onto the commit.
	'''
	if len(argv)>1:
		return ' '.join(argv[2:])
	else:
		return 'Automatic doc commit'
	

def count_words():
	'''
	Count all of the words in the doc
	'''
	system('wc -w docs/doc/doc.md')


def create_doc_pdf():
	'''
	Build the PDF file from the doc markdown file.
	'''
	system('''
		rm doc.pdf; 
		pandoc --toc docs/doc/doc.md -o doc.pdf 2> /dev/null; 
		ls -l doc.pdf
		cp doc.pdf /home/seaman/Dropbox/Shrinking_World/doc
		''')


def doc_files():
	'''	
	List all of the files in the doc using the tree command.
	'''
	print("Get a tree listing of the files")
	system('tree -I env')


def doc_help():
	'''
	Show all the doc commands and their usage.
	'''
	print('''usage: doc doc-command [args]
    doc-commands:

        commit [message args] -- Commit all changes to the doc
        files                 -- List all of the files
        help                  -- Show the available commands
        list                  -- List the parts of the doc
        pdf                   -- Build a PDF file of the doc content
        script                -- List the command scripts
        test                  -- Run all system tests
        words                 -- Count the words
			''')


def doc_list():
	'''
	List the parts of the doc source code.
	'''
	print("List the contents of this doc")
	for d in ['.', 'doc', 'chapters']:
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['pd'],d))))


def doc_script():
	'''
	List the command to work on the doc.
	'''
	print("List the contents of this doc")
	for d in ('bin',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def doc_show():
	'''
	Show the pages of the doc.  Start the server and point the browser to the page.
	'''
	print("Show the doc content in a browswer")

	system('rbg mkdocs serve; sleep 3')
	system('web http://127.0.0.1:8000/doc/Cover/')


def doc_command(argv):
	'''
	Execute all of the doc specific commands
	'''
	if len(argv)>1:

		if argv[1]=='commit':
			commit_command(argv)
			exit(0)

		if argv[1]=='assemble':
			assemble_doc_parts()
			exit(0)

		if argv[1]=='files':
			doc_files()
			exit(0)

		if argv[1]=='list':
			doc_list()
			exit(0)

		if argv[1]=='pdf':
			create_doc_pdf()
			exit(0)

		if argv[1]=='script':
			doc_script()
			exit(0)

		if argv[1]=='show':
			doc_show()
			exit(0)

		if argv[1]=='test':
			system('nosetests -v')
			exit(0)		

		if argv[1]=='words':
			count_words()
			exit(0)

		print('No doc command found, '+argv[1])
		
	doc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	doc_command(argv)