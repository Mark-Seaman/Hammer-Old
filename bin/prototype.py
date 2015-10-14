#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import exists, isfile, join
from random import choice
from sys import argv

from shell import print_banner, print_file_list, enumerate_files


def prototype_add(topic):
    '''Create a new prototype.'''
    path = prototype_add_test(topic)
    system('e '+path)


def prototype_add_test(topic):
    '''Create a new prototype.'''
    if topic:
        path = prototype_path(topic)
        print("New prototype:"+path)
        if exists(path):
            print('File already exists: '+path)
            return path
        with open(path,'w') as f:
            f.write('# prototype: '+topic)
        return path
    else:
        print('Must add a topic')


def prototype_delete(topic):
    '''Delete the prototype.'''
    path = prototype_path(topic)
    print("Delete prototype: "+path)
    if exists(path):
        remove(path)
    else:
        print('File does not exist: '+path)


def prototype_edit(topic):
    '''Edit the content of a prototype.'''
    if not topic:
        print('No topic specified')
        return
    path = prototype_path(topic)
    print("Edit prototype:",path)
    if exists(path):
        system('e '+path)
    else:
        print('File does not exist: '+path)


def prototype_list(topic=None):
    '''List the parts of the prototype source code.'''
    print_file_list(prototype_path(),topic)


def prototype_path(topic=None):
    path = environ['prototype']
    if topic:
        path = join(path,topic)
    return path


def prototype_pick(topic):
    '''Select a topic to edit'''
    system('e '+prototype_path(choice(list(prototype_enumerate()))))


def prototype_show(topic):
    ''' Show the content of a doc.'''
    path = prototype_path(topic)
    for f in enumerate_files(path,topic):
        if isfile(join(path,f)):
            print(f)
            #print_banner (f)
            #print (open(join(path,f)).read().decode('ascii','ignore'))


def get_topic(argv):
    if len(argv)>2:
        return argv[2]
    

def prototype_help():
    '''Show all the prototype prototypes and their usage.'''
    print('''
    usage:  prototype cmd [args]

    cmd:

        add     [file] -- Add a new prototype
        delete  [file] -- Delete a prototype
        edit    [file] -- Edit the prototype
        list    [file] -- List all prototypes
        path    [file] -- Lookup the path for the file
        show    [file] -- Show a prototype
            ''')


def prototype_command(argv):
    '''Execute all of the prototype specific prototypes'''
    if len(argv)>1:

        if argv[1]=='add':
            prototype_add(get_topic(argv))

        elif argv[1]=='add_test':
            prototype_add_test(get_topic(argv))

        elif argv[1]=='delete':
            prototype_delete(get_topic(argv))

        elif argv[1]=='edit':
            prototype_edit(get_topic(argv))

        elif argv[1]=='list':
            prototype_list(get_topic(argv))

        elif argv[1]=='path':
            print(prototype_path(get_topic(argv)))

        elif argv[1]=='pick':
            prototype_pick(get_topic(argv))

        elif argv[1]=='show':
            prototype_show(get_topic(argv))

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

