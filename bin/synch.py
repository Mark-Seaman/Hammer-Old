#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from synch_test import synch_checker

def synch_bin():
	'''Copy the commands to the bin directory'''
	print('synch to the home bin directory')
	project_bin = join(environ['HOME'],'Projects/Hammer/bin')
	home_bin = environ['b']
	synch_sync([ 'synch','bin', project_bin, home_bin])


def synch_copy(argv):
	'''Create a new synch.'''
	print("synch copy: %s %s" % (argv[2],argv[3]))
	system('rsync -auv --existing %s/ %s' % (argv[2],argv[3]))


def synch_mirror(argv):
	'''Delete the synch.'''
	print("synch mirror: %s %s" % (argv[2],argv[3]))
	system('rsync -auv --delete %s/ %s' % (argv[2],argv[3]))


def synch_preview(argv):
	'''Edit the content of a synch.'''
	print("synch preview: %s %s" % (argv[2],argv[3]))
	system('rsync -nauv --delete %s/ %s' % (argv[2],argv[3]))


def synch_help():
	'''Show all the synch synchs and their usage.'''
	print('''
	usage: cmd synch [args]

    synch:

        copy    dir1 dir2 -- Copy the newer files
        preview dir1 dir2 -- Preview the files to be copied
        sync    dir1 dir2 -- Copy the both directions
        mirror  dir1 dir2 -- Make an exact copy
        test              -- Run self test on this file
      
			''')


def synch_sync(argv):
	'''List the parts of the synch source code.'''
	synch_copy(argv)
	synch_copy(argv[:2]+[argv[3],argv[2]])
	

def synch_command(argv):
	'''Execute all of the synch specific synchs'''
	if len(argv)>1:

		if argv[1]=='copy':
			synch_copy(argv)

		elif argv[1]=='bin':
			synch_bin()

		elif argv[1]=='preview':
			synch_preview(argv)

		elif argv[1]=='mirror':
			synch_mirror(argv)

		elif argv[1]=='sync':
			synch_sync(argv)

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