#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv


def vc_commit(argv):
	'''	
	Commit all changes and share with others.
	'''
	comment = argv[2:]
	if not comment:
		comment = 'Automatic commit of Hammer changes'
	else:
		comment = ' '.join(argv[2:])
	print("vc commit:"+comment)
	system('git add -A .; git commit -m"%s"' % comment)


def vc_delete(argv):
	'''	
	Delete the vc.
	'''
	print("Remove files from git",argv[2])
	system('git rm %s' % argv[2])


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
	usage: vc command [args]

    vc:

        commit  [file] -- Add a new vc
        delete  [file] -- Delete a vc
        edit    [file] -- Edit the vc
        status  [file] -- List all vcs
        show    [file] -- Show a vc
      
			''')


def vc_status(argv):
	'''
	List the parts of the vc source code.
	'''
	system('git status')


def vc_show(argv):
	'''	
	Show the content of a vc.
	'''
	system('git diff')


def vc_test(argv):
	'''
	Test the commands for vc
	'''
	print('vc testing is OK')
	system('python $p/bin/vc_test.py')


def vc_command(argv):
	'''
	Execute all of the vc specific vcs
	'''
	if len(argv)>1:

		if argv[1]=='commit':
			vc_commit(argv)
			exit(0)

		if argv[1]=='delete':
			vc_delete(argv)
			exit(0)

		if argv[1]=='edit':
			vc_edit(argv)
			exit(0)

		if argv[1]=='status':
			vc_status(argv)
			exit(0)

		if argv[1]=='show':
			vc_show(argv)
			exit(0)

		if argv[1]=='test':
			vc_test(argv)
			exit(0)

		print('No vc command found, '+argv[1])
		
	vc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	vc_command(argv)
