#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ
from os.path import join
from sys import argv


from dropbox_test import dropbox_checker


def dropbox_add(argv):
    '''Create a new dropbox.'''
    print("New dropbox:"+argv[2])
    system('e bin/'+argv[2])


def dropbox_clean():
    db = join(environ['HOME'],'Documents/Dropbox/Personal/2015')
    files = [f for f in glob(db+'/*') if '(' in f ]
    for f in files:  
        cmd = 'mv "%s" "%s"' % (f,f.replace(db, db+'/old worksheets'))
        print (cmd)
        system (cmd)
   

def dropbox_delete(argv):
    '''Delete the dropbox.'''
    print("dropbox:",argv[2])
    system('rm bin/%s' % argv[2])


def dropbox_edit(argv):
    '''Edit the content of a dropbox.'''
    print("dropbox:",argv[2])
    system('e bin/'+argv[2])


def dropbox_help():
    '''Show all the dropbox dropboxs and their usage.'''
    print('''
    usage: cmd dropbox [args]

    dropbox:

        add     [file] -- Add a new dropbox
        delete  [file] -- Delete a dropbox
        edit    [file] -- Edit the dropbox
        list    [file] -- List all dropboxs
        show    [file] -- Show a dropbox
        test           -- Self test
      
            ''')


def dropbox_list(argv):
    '''List the parts of the dropbox source code.'''
    print("List the contents of this dropbox")
    for d in ('bin',):
        print(d+':')
        print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def dropbox_show(argv):
    '''Show the content of a dropbox.'''
    print("dropbox:",argv[2])
    system('cat bin/%s' % argv[2])


def dropbox_command(argv):
    '''Execute all of the dropbox specific dropboxs'''
    if len(argv)>1:

        if argv[1]=='add':
            dropbox_add(argv)

        elif argv[1]=='clean':
            dropbox_clean()

        elif argv[1]=='delete':
            dropbox_delete(argv)

        elif argv[1]=='edit':
            dropbox_edit(argv)

        elif argv[1]=='list':
            dropbox_list(argv)

        elif argv[1]=='show':
            dropbox_show(argv)

        elif argv[1]=='test':
            dropbox_checker()

        else:
            print('No dropbox command found, '+argv[1])
            dropbox_help()
    else:
        print('No arguments given')
        dropbox_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    dropbox_command(argv)