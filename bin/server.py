#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from server_test import server_checker


def server_add(argv):
	'''Create a new server.'''
	print("New server:"+argv[2])
	system('e bin/'+argv[2])


def server_delete(argv):
	'''Delete the server.'''
	print("server:",argv[2])
	system('rm bin/%s' % argv[2])


def server_edit(argv):
	'''Edit the content of a server.'''
	print("server:",argv[2])
	system('e bin/'+argv[2])


def server_help():
	'''Show all the server servers and their usage.'''
	print('''
	usage: cmd server [args]

    server:

        add     [file] -- Add a new server
        delete  [file] -- Delete a server
        edit    [file] -- Edit the server
        list    [file] -- List all servers
        show    [file] -- Show a server
        test           -- Self test
      
			''')


def server_list(argv):
	'''List the parts of the server source code.'''
	print("List the contents of this server")
	for d in ('bin',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def server_show(argv):
	'''Show the content of a server.'''
	print("server:",argv[2])
	system('cat bin/%s' % argv[2])


def server_command(argv):
	'''Execute all of the server specific servers'''
	if len(argv)>1:

		if argv[1]=='add':
			server_add(argv)

		elif argv[1]=='delete':
			server_delete(argv)

		elif argv[1]=='edit':
			server_edit(argv)

		elif argv[1]=='list':
			server_list(argv)

		elif argv[1]=='show':
			server_show(argv)

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