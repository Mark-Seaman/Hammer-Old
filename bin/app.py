#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import exists, isfile, join
from random import choice
from sys import argv

from shell import enumerate_files, print_file, print_file_list, print_banner
from shell import delete_file, edit_file, add_file, show_files


def app_path(topic=None):
    path = environ['pa']
    if topic:
        path = join(path,topic+'.py')
    return path
    

def app_help():
    '''Show all the app apps and their usage.'''
    print('''
    usage:  app cmd [args]

    cmd:

        db             -- Do a syncdb operation
        edit    file   -- Edit the app
        list    [file] -- List all app source code files
        path    [file] -- Lookup the path for the file
        search  text   -- Find text in the source code
        show    [file] -- Show a app source code file
            ''')


def kill_server():
    cmd = '''x=`ps -ef | grep -v grep | grep runserver | awk '{ print $2 }'`
        [ ! -z "$x" ]  && echo kill $x   && kill $x'''
    system(cmd)


def list_files(topic):
    '''List the source code for the app'''
    files =enumerate_files(app_path(),topic)
    files = [f for f in files if f.endswith('.py')]
    print ('\n'.join(sorted(files)))


def run_server():
    system('''
            cd $pa;
            rbg python manage.py runserver;
            sleep 2
            web http://127.0.0.1:8000/;
           ''')


def app_command(argv):
    '''Execute all of the app specific apps'''
    if len(argv)>1:

        if len(argv)>2:
            topic = argv[2]
        else:
            topic = None
         
        if argv[1]=='add':
            add_file(app_path(), argv[2])    
            app_edit(topic)

        elif argv[1]=='add_test':
            add_file(app_path(), argv[2])    

        elif argv[1]=='db':
            system('cd $pa; python manage.py syncdb')

        elif argv[1]=='delete':
            delete_file(app_path(argv[2]))

        elif argv[1]=='edit':
            edit_file(app_path(argv[2]))

        elif argv[1]=='kill':
            kill_server()

        elif argv[1]=='list':
            list_files(topic)

        elif argv[1]=='path':
            print(app_path(topic))

        elif argv[1]=='pick':
            system('e '+app_path(choice(list(app_enumerate()))))

        elif argv[1]=='run':
            run_server()

        elif argv[1]=='search':
            system('grep %s $pa/*/*.py' % argv[2])

        elif argv[1]=='show':
            show_files(app_path(),topic)

        else:
            print('No app command found, '+argv[1])
            app_help()
    else:
        print('No arguments given')
        app_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    app_command(argv)

