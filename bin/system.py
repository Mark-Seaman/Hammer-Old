#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join,exists
from sys import argv

from system_test import system_checker


def system_add(argv):
    '''Create a new system.'''
    f = join(environ['b'],argv[2])
    if exists(f):
        print('File exists, '+f)
    else:
        print("New system script: "+f)
        system('touch ' + f)
        system('exe ' + f)
        system('e ' + f)


def system_delete(argv):
    '''Delete the system.'''
    f = join(environ['b'],argv[2])
    if not exists(f):
        print('No file exists, '+f)
    else:
        print("rm " + f)
        system('rm ' + f)


def system_edit(argv):
    '''Edit the content of a system.'''
    print("system:",argv[2])
    system('e bin/'+argv[2])


def system_help():
    '''Show all the system systems and their usage.'''
    print('''
    usage: system cmd [args]

    system:

        add     [file] -- Add a new system script
        delete  [file] -- Delete a system script
        edit    [file] -- Edit the system script
        list    [file] -- List all system scripts
        show    [file] -- Show a system script
        test           -- Self test all the scripts
      
            ''')


def system_list(argv):
    '''List the parts of the system source code.'''
    print("List the contents of this system")
    for d in ('bin',):
        print(d+':')
        print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def system_show(argv):
    '''Show the content of a system.'''
    print("system:",argv[2])
    system('cat bin/%s' % argv[2])


def system_command(argv):
    '''Execute all of the system specific systems'''
    if len(argv)>1:

        if argv[1]=='add':
            system_add(argv)

        elif argv[1]=='delete':
            system_delete(argv)

        elif argv[1]=='edit':
            system_edit(argv)

        elif argv[1]=='list':
            system_list(argv)

        elif argv[1]=='show':
            system_show(argv)

        elif argv[1]=='test':
            system_checker()

        else:
            print('No system command found, '+argv[1])
            system_help()
    else:
        print('No arguments given')
        system_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    system_command(argv)