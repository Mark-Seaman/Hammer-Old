#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ
from os.path import join, exists, isfile
from os import chmod
import stat
from sys import argv

from shell import shell


def command_add_script(command):
	'''Create the executable shell command that runs the python command'''
	script = '''#!/bin/bash
# Execute a %s script command

python $p/bin/%s.py $*

	''' % (command,command)
	path = join(environ['pb'],'%s' % command)
	if exists(path):
		print('File already exists: '+path)
	else:
		with open(path,'w') as f:
			f.write(script)
	chmod (path, stat.S_IRWXU|stat.S_IRGRP|stat.S_IROTH)


def command_add(argv):
	'''Create a new command.'''
	print("Add new command:"+argv[2])
	command = argv[2]
	command_add_script(command)
	script_path = join(environ['pb'],'%s.py' % command)
	template_path = join(environ['pb'],'prototype.py')
	command_content = open(template_path).read().replace('prototype',command)
	#print('Content: %s.py \n %s' % (command,command_content))
	if exists(script_path):
		print('File already exists: '+script_path)
	else:
		with open(script_path,'w') as f:
			f.write(command_content)
		system('tst add ' + command)
	#command_edit(argv)


def command_delete(argv):
	'''	Delete the command.'''
	print("Command:",argv[2])
	print(shell('rm bin/%s.py' % argv[2]))
	print(shell('rm bin/%s' % argv[2]))


def command_edit(argv):
	'''	Edit the content of a command.'''
	print("Command edit: " + argv[2])
	print(shell('e $p/bin/%s.py' % argv[2]))


def command_function(argv):
	if not argv:
		print 'No function requested'
	path = join(environ['pb'],argv[0]+'.py')
	if not exists(path):
		print('Command not found: '+path)
	else:
		print("Command:",path)
		text = """

# New code for function

		yyy  -- Do it

        elif argv[1]=='yyy':
			xxx_yyy(argv[2:])


def xxx_yyy(argv):
	'''	Edit the content of a command.'''
	print("xxx yyy: " + argv[0])
	print(shell('echo $p/bin/%s.py %s' % (argv[0], argv[1])))


		""".replace('xxx', argv[0]).replace('yyy', argv[1])
		open(path, 'a').write(text)



def command_help():
	'''Show all the command commands and their usage.'''
	print('''
	usage: cmd command [args]

    command:

        add     [file] -- Add a new command
        delete  [file] -- Delete a command
        edit    [file] -- Edit the command
        list    [file] -- List all commands
        search  [pattern] -- Find the pattern in commands
        show    [file] -- Show a command
        test           -- Run the self-test
      
			''')


def command_list(argv):
	'''List the parts of the command source code.'''
	path = join(environ['p'],'bin')
	files =  [f for f in glob(path+'/*.py') if not f.endswith('_test.py')]
	files =  [f[len(path)+1:] for f in sorted(files)]
	print('\n'.join(files))


def command_search(argv):
	'''Search the commands for the requested text'''
	pattern = ' '.join(argv)
	print('cmd search:  '+pattern)
	system('grep ' + pattern + ' $pb/*.py')


def command_show(argv):
	'''	Show the content of a command.'''
	path = join(environ['pb'],argv[2]+'.py')
	if not exists(path):
		print('Command not found: '+path)
	else:
		print("Command:",path)
		print(open(path).read())


def cmd_command(argv):
	'''Execute all of the command specific commands'''
	if len(argv)>1:

		if argv[1]=='add-test':
			command_add(argv)

		elif argv[1]=='add':
			command_add(argv)
			command_edit(argv)

		elif argv[1]=='delete':
			command_delete(argv)

		elif argv[1]=='edit':
			command_edit(argv)

		elif argv[1]=='function':
			command_function(argv[2:])

		elif argv[1]=='list':
			command_list(argv)

		elif argv[1]=='search':
			command_search(argv[2:])

		elif argv[1]=='show':
			command_show(argv)

		else:
			print('No command command found, '+argv[1])
			command_help()

	else:
		command_help()


'''Create a script that can be run from the shell'''
if __name__=='__main__':
 	cmd_command(argv)