#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from code_test import code_checker


def code_add(argv):
	'''Create a new code.'''
	print("New code:"+argv[2])
	system('e bin/'+argv[2])


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

from glob import glob
from os import chdir

def code_list(argv):
	'''List the parts of the code source code.'''
	for d in ('bin',):
		chdir(environ['p'])
		files = [f for f in glob(d+'/*') if not f.endswith('.pyc')]
		print('\n'.join(files))


def code_show(argv):
	'''Show the content of a code.'''
	print("code:",argv[2])
	system('cat bin/%s' % argv[2])


def code_command(argv):
	'''Execute all of the code specific codes'''
	if len(argv)>1:

		if argv[1]=='add':
			code_add(argv)

		elif argv[1]=='delete':
			code_delete(argv)

		elif argv[1]=='edit':
			code_edit(argv)

		elif argv[1]=='list':
			code_list(argv)

		elif argv[1]=='show':
			code_show(argv)

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