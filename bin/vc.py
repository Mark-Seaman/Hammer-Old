#!/usr/bin/env python

from os import chdir, system, listdir, environ
from os.path import join
from sys import argv

from shell import on_internet


def vc_changes():
    '''Form the shell script for the commit command. '''
    print('List all pending changes to the tracked files')
    system('cd $p; git diff --no-color --word-diff')


def vc_commit(comment):
	'''	
	Commit all changes and share with others.
	'''
	commit_command = '''#!/bin/bash
	# Commit all changes to the remote repo
	cd $p
	git add -A .        &&  
	git commit -m"%s"   
	git pull            &&
	git push
	'''

	if not on_internet():
		print ("Need an internet connection")
	elif not comment:
		print ("Must have a comment") 
	else:
		#chdir(environ['p'])
		system(commit_command % ' '.join(comment))


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
        status  [file] -- List all files with pending changes
      
			''')


def vc_status(argv):
	'''
	List the parts of the vc source code.
	'''
	system('git status')


def vc_command(argv):
	'''
	Execute all of the vc specific vcs
	'''
	if len(argv)>1:

		if argv[1]=='changes':
			vc_changes()

		elif argv[1]=='commit':
			vc_commit(argv[2:])

		elif argv[1]=='delete':
			vc_delete(argv)

		elif argv[1]=='help':
			vc_help()

		elif argv[1]=='status':
			vc_status(argv)

		else:
			vc_commit(argv[2:])
	else:
		vc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	vc_command(argv)
