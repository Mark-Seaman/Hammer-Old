#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ, chdir
from os.path import join, isdir
from sys import argv

from code_test import code_checker


def code_add(argv):
	'''Create a new code.'''
	print("New code:"+argv[2])
	system('e bin/'+argv[2])


def code_complexity(files=None):
	'''Measure the code complexity'''
	print ('code_complexity:',files)
	if not files:
		files = code_list().split('\n')
	for f in files:
		text = open(join(environ['p'],f)).read()
		print('Lines: ',len(text.split('\n')), f)
		

def code_delete(argv):
	'''Delete the code.'''
	print("code:",argv[2])
	system('rm bin/%s' % argv[2])


def code_edit(argv):
	'''Edit the content of a code.'''
	print("code:",argv[2])
	system('e bin/'+argv[2])


def code_help():
	'''Show all the code codes and their usage.'''
	print('''
	usage: cmd code [args]

    code:

        add     [file] -- Add a new code
        delete  [file] -- Delete a code
        edit    [file] -- Edit the code
        list    [file] -- List all codes
        show    [file] -- Show a code
        test           -- Self test
      
			''')



def code_list(files=None):
	'''List the files of source code.'''
	results = []
	if not files:
		files = ['bin']
	for d in files:
		chdir(environ['p'])
		files = [f for f in glob(d+'/*') if not isdir(f)]
		files = [f for f in files if not f.endswith('.pyc')]
		results.append('\n'.join(files))
	return '\n'.join(results)


def code_show(files):
	'''Show the content of a code.'''
	print("code:",files)
	if not files:
		files = code_list().split('\n')
	for f in files:
		system('cat %s' % f)


def code_command(argv):
	'''Execute all of the code specific codes'''
	if len(argv)>1:

		if argv[1]=='add':
			code_add(argv)

		elif argv[1]=='complexity':
			code_complexity()

		elif argv[1]=='delete':
			code_delete(argv)

		elif argv[1]=='edit':
			code_edit(argv)

		elif argv[1]=='list':
			print(code_list())

		elif argv[1]=='show':
			code_show(argv[2:])

		elif argv[1]=='test':
			code_checker()

		else:
			print('No code command found, '+argv[1])
			code_help()
	else:
		print('No arguments given')
		code_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	code_command(argv)