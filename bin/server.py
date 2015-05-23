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
	print("server console:"+argv[2])
	#system('e bin/'+argv[2])


def server_deploy(argv):
	'''Deploy code on the server'''
	print("server deploy:"+argv[2])
	#system('e bin/'+argv[2])

	
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
	print("server host: ",)
	server_do(' hostname')


def server_restart(argv):
	'''Run a command on the server'''
	print("server restart:"+argv[2])
	#system('e bin/'+argv[2])


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
			server_console(argv)

		elif argv[1]=='deploy':
			server_deploy(argv)

		elif argv[1]=='do':
			command = ' '.join(argv[2:])
			server_do(command)

		elif argv[1]=='host':
			server_host()

		elif argv[1]=='restart':
			server_restart(argv)

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