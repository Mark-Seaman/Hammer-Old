#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import exists, isfile, join
from random import choice
from sys import argv

from shell import enumerate_files, print_file, print_file_list, print_banner
from shell import delete_file, edit_file, add_file, show_files
from store import save, recall, key_name


def switches_list():
    return [ x.strip() for x in '''
            ON_INTERNET 
            REDIS_KEY
            SHOW_WEB_PAGE
        '''.split('\n')[1:-1] ]


def switches_get(switch):
    return recall(key_name(switch))=='True'


def switches_set(switch, value):
    if value:
        return save(key_name(switch), 'True')
    else:
        return save(key_name(switch), 'False')


def switches_path():
    return join(environ['pb'],'settings-private')
    

def switches_help():
    '''Show all the switches switchess and their usage.'''
    print('''
    usage:  switches cmd [args]

    cmd:

        edit    - Edit the switches
        list    - List all switches
        path    - Lookup the path for the file
        load    - Show a switches
            ''')


def load_switches():
    '''Load the shell variables into redis'''
    for s in switches_list():
        switches_set(s, environ[s]=="True" )


def list_switches():
    '''Load the shell variables into redis'''
    for s in switches_list():
        print('%s=%s' % (s,switches_get(s)))


def switches_command(argv):
    '''Execute all of the switches specific switches'''
    if len(argv)>1:

        if len(argv)>2:
            topic = argv[2]
        else:
            topic = None
         
        if argv[1]=='edit':
            edit_file(switches_path())

        elif argv[1]=='list':
            list_switches()

        elif argv[1]=='path':
            print(switches_path())

        elif argv[1]=='load':
            load_switches()

        else:
            print('No switches command found, '+argv[1])
            switches_help()
    else:
        print('No arguments given')
        switches_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    switches_command(argv)

