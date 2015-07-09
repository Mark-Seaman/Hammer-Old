#!/usr/bin/env python

from os import system, listdir, environ, walk, rename
from os.path import join,isdir
from sys import argv

from music_test import music_checker


def music_add(argv):
    '''Create a new music.'''
    print("New music:"+argv[2])
    system('e bin/'+argv[2])


def music_delete(argv):
    '''Delete the music.'''
    print("music:",argv[2])
    system('rm bin/%s' % argv[2])


def music_edit(argv):
    '''Edit the content of a music.'''
    print("music:",argv[2])
    system('e bin/'+argv[2])


def music_help():
    '''Show all the music musics and their usage.'''
    print('''
    usage: cmd music [args]

    music:

        add     [file] -- Add a new music
        delete  [file] -- Delete a music
        edit    [file] -- Edit the music
        list    [file] -- List all musics
        rename         -- Rename files with "_"
        save           -- Copy files in new to rock
        show    [file] -- Show a music
        test           -- Self test
      
            ''')

# Recursive list
def recursive_list(root_dir):
    '''List the files in a directory tree.'''
    matches = []
    for root, dirnames, filenames in walk(root_dir):
        for filename in filenames:
            matches.append(join(root, filename).replace(root_dir+'/',''))
    return matches


def directory_list(root_dir):
    '''List the directories in a directory tree.'''
    matches = []
    for root, dirnames, filenames in walk(root_dir):
        for dirname in dirnames:
            matches.append(join(root, dirname).replace(root_dir+'/',''))
    return matches
   

def music_list(argv):
    print("List the contents of this music")
    print ("Tracks:" + '\n'.join(recursive_list("../Music/new")))


def music_rename():
    # Rename directories
    for f in directory_list("../Music/new"):
        f1 = join("../Music/new",f)
        f2 = f1.replace('_',' ')
        print('rename directory:  '+f1+' '+f2)
        rename(f1, f2)
    # Rename files
    for f in recursive_list("../Music/new"):
        if '_' in f:
            f1 = join("../Music/new",f)
            f2 = f1.replace('_',' ')
            print('rename file:  '+f1+' '+f2)
            rename(f1, f2)


def music_save():
    system('cptree ~/Music/new $rock; music-commit')


def music_show(argv):
    '''Show the content of a music.'''
    print("music:",argv[2])
    system('cat bin/%s' % argv[2])


def music_command(argv):
    '''Execute all of the music specific musics'''
    if len(argv)>1:

        if argv[1]=='add':
            music_add(argv)

        elif argv[1]=='delete':
            music_delete(argv)

        elif argv[1]=='edit':
            music_edit(argv)

        elif argv[1]=='list':
            music_list(argv)

        elif argv[1]=='rename':
            music_rename()

        elif argv[1]=='save':
            music_save()

        elif argv[1]=='show':
            music_show(argv)

        elif argv[1]=='test':
            music_checker()

        else:
            print('No music command found, '+argv[1])
            music_help()
    else:
        print('No arguments given')
        music_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    music_command(argv)