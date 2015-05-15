#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from synch_test import synch_checker


def synch_add(argv):
	'''Create a new synch.'''
	print("New synch:"+argv[2])
	system('e bin/'+argv[2])


def synch_delete(argv):
	'''Delete the synch.'''
	print("synch:",argv[2])
	system('rm bin/%s' % argv[2])


def synch_edit(argv):
	'''Edit the content of a synch.'''
	print("synch:",argv[2])
	system('e bin/'+argv[2])


def synch_help():
	'''Show all the synch synchs and their usage.'''
	print('''
	usage: cmd synch [args]

    synch:

        add     [file] -- Add a new synch
        delete  [file] -- Delete a synch
        edit    [file] -- Edit the synch
        list    [file] -- List all synchs
        show    [file] -- Show a synch
        test           -- Run self test on this file
      
			''')


def synch_list(argv):
	'''List the parts of the synch source code.'''
	print("List the contents of this synch")
	for d in ('bin',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def synch_show(argv):
	'''Show the content of a synch.'''
	print("synch:",argv[2])
	system('cat bin/%s' % argv[2])


def synch_command(argv):
	'''Execute all of the synch specific synchs'''
	if len(argv)>1:

		if argv[1]=='add':
			synch_add(argv)

		elif argv[1]=='delete':
			synch_delete(argv)

		elif argv[1]=='edit':
			synch_edit(argv)

		elif argv[1]=='list':
			synch_list(argv)

		elif argv[1]=='show':
			synch_show(argv)

		elif argv[1]=='test':
			synch_checker()

		else:
			print('No synch command found, '+argv[1])
			synch_help()
	else:
		print('No arguments given')
		synch_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	synch_command(argv)