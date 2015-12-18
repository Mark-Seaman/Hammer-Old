#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import exists, isfile, join
from platform import node
from random import choice
from sys import argv

from shell import enumerate_files, print_file, print_file_list, print_banner
from shell import delete_file, edit_file, add_file, show_files


def web(page):
    '''Open a web page in Google Chrome'''
    url = page
    if not page.startswith('http://') and not page.startswith('https://'):
        url = 'http://' + page
    # Use the correct invocation
    if 'mac' in node() or 'mini' in node():
        system('open -a "Google Chrome" '+url)
    else:
        system('rbg google-chrome '+url)


def web_path(topic=None):
    path = environ['pb']
    if topic:
        path = join(path,topic)
    return path
    

def web_help():
    '''Show all the web webs and their usage.'''
    print('''
    usage:  web cmd [args]

    cmd:

        github  -- Go the Github site
        gmail   -- Gmail
        issues  -- Track issues for project
        wiki    -- Go to Github wiki

            ''')

def web_command(argv):
    '''Execute all of the web specific webs'''
    if len(argv)>1:

        if len(argv)>2:
            topic = argv[2]
        else:
            topic = None
         
        if argv[1]=='github':
            web('https://github.com')

        elif argv[1]=='gmail':
            web('gmail.com')
           
        elif argv[1]=='issues':
            web('https://github.com')

        elif argv[1]=='wiki':
            web('https://github.com')

        else:
            web(argv[1])
    else:
        print('No arguments given')
        web_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    web_command(argv)

