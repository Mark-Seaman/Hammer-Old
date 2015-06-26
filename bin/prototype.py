#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from prototype_test import prototype_checker


def prototype_add(argv):
    '''Create a new prototype.'''
    print("New prototype:"+argv[2])
    system('e bin/'+argv[2])


def prototype_delete(argv):
    '''Delete the prototype.'''
    print("prototype:",argv[2])
    system('rm bin/%s' % argv[2])


def prototype_edit(argv):
    '''Edit the content of a prototype.'''
    print("prototype:",argv[2])
    system('e bin/'+argv[2])


def prototype_help():
    '''Show all the prototype prototypes and their usage.'''
    print('''
    usage: cmd prototype [args]

    prototype:

        add     [file] -- Add a new prototype
        delete  [file] -- Delete a prototype
        edit    [file] -- Edit the prototype
        list    [file] -- List all prototypes
        show    [file] -- Show a prototype
        test           -- Self test
      
            ''')


def prototype_list(argv):
    '''List the parts of the prototype source code.'''
    print("List the contents of this prototype")
    for d in ('bin',):
        print(d+':')
        print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def prototype_show(argv):
    '''Show the content of a prototype.'''
    print("prototype:",argv[2])
    system('cat bin/%s' % argv[2])


def prototype_command(argv):
    '''Execute all of the prototype specific prototypes'''
    if len(argv)>1:

        if argv[1]=='add':
            prototype_add(argv)

        elif argv[1]=='delete':
            prototype_delete(argv)

        elif argv[1]=='edit':
            prototype_edit(argv)

        elif argv[1]=='list':
            prototype_list(argv)

        elif argv[1]=='show':
            prototype_show(argv)

        elif argv[1]=='test':
            prototype_checker()

        else:
            print('No prototype command found, '+argv[1])
            prototype_help()
    else:
        print('No arguments given')
        prototype_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    prototype_command(argv)