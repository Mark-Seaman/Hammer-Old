#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join,exists
from sys import argv


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


def system_commit(argv):
    '''Do a big commit with the provided comment'''
    comment = 'Auto commit all changes in Documents '
    if len(argv)>2:
        comment = ' '.join(argv[2:])
    command = '''echo Commit all changes to documents
        cd $HOME/Documents
        git add -A . &&
        git commit -m"%s" &&
        git pull &&
        git push
    ''' % comment
    system(command)


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
    f = join(environ['b'],argv[2])
    if not exists(f):
        print('No file exists, '+f)
    else:
        system('e '+f)


def system_help():
    '''Show all the system systems and their usage.'''
    print('''
    usage: system cmd [args]

    system:

        add     [file] -- Add a new system script
        commit  [comment] -- Words for git commit comments
        delete  [file] -- Delete a system script
        edit    [file] -- Edit the system script
        list    [file] -- List all system scripts
        show    [file] -- Show a system script
        test           -- Self test all the scripts
      
            ''')



def system_list(argv):
    '''List the parts of the system source code.'''
    for p in listdir(environ['b']):
        print(p)


def system_show(argv):
    '''Show the content of a system.'''
    f = join(environ['b'],argv[2])
    if not exists(f):
        print('No file exists, '+f)
    else:
        system('echo File Contents: '+f)
        system('cat '+f)


def system_disk_usage():
    '''Get the disk usage for the home directory'''
    system ('du -s $HOME $HOME/* | sort -nr')


def system_disk_free():
    '''Get the disk usage for the home directory'''
    system ('df -h $HOME')


def system_command(argv):
    '''Execute all of the system specific systems'''
    if len(argv)>1:

        if argv[1]=='add':
            system_add(argv)

        elif argv[1]=='commit':
            system_commit(argv)

        elif argv[1]=='delete':
            system_delete(argv)

        elif argv[1]=='edit':
            system_edit(argv)
        
        elif argv[1]=='free':
            system_disk_free()

        elif argv[1]=='list':
            system_list(argv)

        elif argv[1]=='show':
            system_show(argv)

        elif argv[1]=='usage':
            system_disk_usage()

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