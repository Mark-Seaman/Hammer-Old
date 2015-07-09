#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from server_test import server_checker
from tst import shell


def server_changes():
	'''Show the pending changes on the server'''
	print("server changes:")
	server_do('cd Documents; git status; hostname')


def server_console():
	'''Show the console on the server'''
	print("server console: ssh ubuntu@seamantech.com")
	system('ssh ubuntu@seamantech.com')


def server_deploy(argv):
	'''Deploy code to the server'''
	print("server deploy:")
	system('''# Local operations
		cd ~/Projects/seamantech
		git add -A . 
		git commit -m 'Deploy the Hammer code'
		git pull && git push
		''')
	server_do('''# Remote operations
		cd ~/Projects/seamantech
		hostname &&
		pwd &&
		git pull
		''')
	server_restart()
	
	
def server_do(command):
	'''Run a command on the server'''
	#print("server do: "+command)
	system('ssh '+environ['ph']+' "'+command+'"')

	
def server_help():
	'''Show all the server servers and their usage.'''
	print('''
	usage: server cmd  [args]

    server:

        changes		-- show pending changes
        console		-- run a console window for the server
        deploy 		-- deploy the server code
        do          -- run a shell command on the remote server
        host     	-- get the hostname of the server
        restart		-- restart the web server
        status		-- show the remote server status
        test        -- Self test
      
			''')


def server_host():
	'''Run hostname command on the server'''
	server_do(' hostname')


def server_publish():
	'''Push the documents to the server'''
	print("server publish:")
	system('''# Local operations
		cd ~/Documents
		git add -A . 
		git commit -m 'Publish my book'
		git pull && git push
		''')
	server_do('''# Remote operations
		hostname &&
		cd ~/Documents &&
		pwd &&
		git pull
		''')
	

def server_restart():
	'''Run a command on the server'''
	print("server restart:")
	server_do('~/base-bin/restart-apache')


def server_status():
	'''Show the status of the server'''
	print("server status:")
	server_do('ps -ef|grep apache; hostname')


def server_command(argv):
	'''Execute all of the server specific servers'''
	if len(argv)>1:

		if argv[1]=='changes':
			server_changes()

		elif argv[1]=='console':
			server_console()

		elif argv[1]=='deploy':
			server_deploy(argv)

		elif argv[1]=='do':
			command = ' '.join(argv[2:])
			server_do(command)

		elif argv[1]=='host':
			server_host()

		elif argv[1]=='publish':
			server_publish()

		elif argv[1]=='restart':
			server_restart()

		elif argv[1]=='status':
			server_status()

		elif argv[1]=='test':
			server_checker()

		else:
			print('No server command found, '+argv[1])
			server_help()
	else:
		print('No arguments given')
		server_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	server_command(argv)