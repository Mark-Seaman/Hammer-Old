#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import exists, isfile, join
from random import choice
from sys import argv

from shell import enumerate_files, print_file, print_file_list, print_banner
from shell import delete_file, edit_file, add_file, show_files


def prototype_path(topic=None):
    path = environ['pb']
    if topic:
        path = join(path,topic)
    return path
    

def prototype_help():
    '''Show all the prototype prototypes and their usage.'''
    print('''
    usage:  prototype cmd [args]

    cmd:

        add     [file] - Add a new prototype
        delete  [file] - Delete a prototype
        edit    [file] - Edit the prototype
        list    [file] - List all prototypes
        path    [file] - Lookup the path for the file
        show    [file] - Show a prototype
            ''')


def prototype_command(argv):
    '''Execute all of the prototype specific prototypes'''
    if len(argv)>1:

        if len(argv)>2:
            topic = argv[2]
        else:
            topic = None
         
        if argv[1]=='add':
            add_file(prototype_path(), argv[2])    
            prototype_edit(topic)

        elif argv[1]=='add_test':
            add_file(prototype_path(), argv[2])    

        elif argv[1]=='delete':
            delete_file(prototype_path(argv[2]))

        elif argv[1]=='edit':
            edit_file(prototype_path(argv[2]))

        elif argv[1]=='list':
            print_file_list(prototype_path(),topic)

        elif argv[1]=='path':
            print(prototype_path(topic))

        elif argv[1]=='pick':
            system('e '+prototype_path(choice(list(prototype_enumerate()))))

        elif argv[1]=='show':
            show_files(prototype_path(),topic)

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

