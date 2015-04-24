#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv


def vc_add(argv):
	'''	
	Create a new vc.
	'''
	print("New vc:"+argv[2])
	system('git add -A .; git commit -m"%s"' % argv[2])


def vc_delete(argv):
	'''	
	Delete the vc.
	'''
	print("vc: rm not implemented: ",argv[2])


def vc_edit(argv):
	'''	
	Edit the content of a vc.
	'''
	print("vc: edit not implemented: ",argv[2])


def vc_help():
	'''
	Show all the vc vcs and their usage.
	'''
	print('''
	usage: cmd vc [args]

    vc:

        add     [file] -- Add a new vc
        delete  [file] -- Delete a vc
        edit    [file] -- Edit the vc
        list    [file] -- List all vcs
        show    [file] -- Show a vc
      
			''')


def vc_list(argv):
	'''
	List the parts of the vc source code.
	'''
	system('git diff')


def vc_show(argv):
	'''	
	Show the content of a vc.
	'''
	system('git status')


def vc_command(argv):
	'''
	Execute all of the vc specific vcs
	'''
	if len(argv)>1:

		if argv[1]=='add':
			vc_add(argv)
			exit(0)

		if argv[1]=='delete':
			vc_delete(argv)
			exit(0)

		if argv[1]=='edit':
			vc_edit(argv)
			exit(0)

		if argv[1]=='list':
			vc_list(argv)
			exit(0)

		if argv[1]=='show':
			vc_show(argv)
			exit(0)

		print('No vc vc found, '+argv[1])
		
	vc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	vc_command(argv)
