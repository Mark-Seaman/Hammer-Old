#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from vc_test import vc_checker



def vc_changes():
    '''Form the shell script for the commit command. '''
    print('List all pending changes to the book')
    system('cd $p; git diff --color-words --word-diff')


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
	system('commit %s "%s"' % (environ['p'], comment))


def vc_delete(argv):
	'''	
	Delete the vc.
	'''
	print("Remove files from git",argv[2])
	system('git rm %s' % argv[2])


def vc_help():
	'''
	Show all the vc vcs and their usage.
	'''
	print('''
	usage: vc command [args]

    vc:

        changes        -- Run git diff to show changes
        commit  [file] -- Add a new vc
        delete  [file] -- Delete a vc
        help    [file] -- See the vc commands
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
	

def vc_command(argv):
	'''
	Execute all of the vc specific vcs
	'''
	if len(argv)>1:

		if argv[1]=='changes':
			vc_changes()

		elif argv[1]=='commit':
			vc_commit(argv)

		elif argv[1]=='delete':
			vc_delete(argv)

		elif argv[1]=='help':
			vc_help()

		elif argv[1]=='status':
			vc_status(argv)

		elif argv[1]=='show':
			vc_show(argv)

		elif argv[1]=='test':
			vc_checker()

		else:
			print('No vc command found, '+argv[1])
			vc_commit(['commit']+argv)
	else:
		vc_commit(['commit'])


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	vc_command(argv)
