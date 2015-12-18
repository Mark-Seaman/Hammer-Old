#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import join, exists
from random import choice
from sys import argv

from shell import enumerate_files, print_file_list

def ocean_add(topic):
    '''Create a new ocean.'''
    if topic:
        path = ocean_path(topic)
        print("New ocean:"+path)
        if exists(path):
            print('File already exists: '+path)
        else:
            with open(path,'w') as f:
                f.write('# ocean: '+topic)
        system('e '+path)
    else:
        print('Must add a topic')


def ocean_code():
    return 'root@%s:/home/django/django_project' % ocean_ip()


def ocean_console():
    '''Login to the remote droplet'''
    system ('ssh root@%s' % ocean_ip())


def ocean_control():
    '''Control panel to the remote droplet'''
    system ('web https://cloud.digitalocean.com/droplets/')


def ocean_delete(topic):
    '''Delete the ocean.'''
    path = ocean_path(topic)
    print("Delete ocean: "+path)
    if exists(path):
        remove(path)
    else:
        print('File does not exist: '+path)

    #cmd = 'ssh root@%s service nginx restart' % ocean_ip()
    cmd = 'ssh root@%s service gunicorn restart' % ocean_ip()
    system(cmd)
    print(cmd)

def ocean_deploy():
    from_dir = ocean_path()
    to_dir = ocean_code()
    #cmd = 'rsync -auv --delete %s/ %s' % (from_dir, to_dir)
    cmd = 'rsync -auv %s/ %s' % (from_dir, to_dir)
    system(cmd)
    print(cmd)
    cmd = 'ssh root@%s service gunicorn restart' % ocean_ip()
    system(cmd)
    print(cmd)


def ocean_doc(topic=None):
    path = environ['mybook']
    if topic:
        path = join(path,topic)
    return path


def ocean_edit(topic):
    '''Edit the content of a ocean.'''
    if not topic:
        print('No topic specified')
        return
    path = ocean_path(topic)
    print("Edit ocean:",path)
    if exists(path):
        system('e '+path)
    else:
        print('File does not exist: '+path)


def ocean_get_code():
    print('rsync -auv %s/ %s' % (ocean_code(), ocean_path()))


def ocean_help():
    '''Show all the ocean oceans and their usage.'''
    print('''
    usage: cmd ocean [args]

    ocean:

        add     [file] -- Add a new ocean
        code           -- Directory for remote code
        control        -- Go to the control panel
        console        -- Console login
        deploy         -- Copy the code to the remote droplet
        delete  [file] -- Delete a ocean
        edit    [file] -- Edit the ocean
        getcode        -- Copy the code from the remote droplet
        list    [file] -- List all oceans
        path    [file] -- Lookup the path for the file
        runserver      -- Start up the development server
        show    [file] -- Show a ocean
        summary        -- Show a summary of documents
        web            -- Web page for droplet
            ''')


def ocean_ip():
    return '127.0.0.1'


def ocean_list(topic=None):
    '''List the parts of the ocean source code.'''
    print('App:')
    print_file_list(ocean_path())
    print('Docs:')
    #print_file_list(ocean_doc())
    code = [ f for f in enumerate_files(ocean_path())]
    docs = [ f for f in enumerate_files(ocean_doc())]
    print ('Summary: %d code files, %d doc files' % (len(code), len(docs)))


def ocean_path(topic=None):
    path = join(environ['p'],'app')
    if topic:
        path = join(path,topic)
    return path


def ocean_pick(topic):
    '''Select a topic to edit'''
    system('e '+ocean_path(choice(list(ocean_enumerate()))))


def ocean_publish():
    path1 = ocean_doc()
    path2 = join(ocean_code(),'user_doc')
    system('rsync -auv --delete %s/ %s' % (path1, path2)) 


def ocean_show(topic):
    '''Show the content of a ocean.'''
    if topic:
        path = ocean_path(topic)
        print("Show ocean: "+path)
        if exists(path):
            print(open(path).read())
            return
        print('File does not exists: '+path)
    else:
        print('No topic listed')


def ocean_view(topic):
    '''Open the web page for the remote droplet'''
    if topic:
        system ('web http://localhost:8000/'+topic)
    else:
        system ('web http://localhost:8000/Index')


def ocean_web(topic=None):
    '''Open the web page for the remote droplet''' 
    system ('web http://'+ocean_ip())


def get_topic(argv):
    if len(argv)>2:
        return argv[2]
    

def ocean_command(argv):
    '''Execute all of the ocean specific oceans'''
    if len(argv)>1:

        if argv[1]=='add':
            ocean_add(get_topic(argv))

        elif argv[1]=='code':
            print(ocean_code())

        elif argv[1]=='console':
            ocean_console()

        elif argv[1]=='control':
            ocean_control()

        elif argv[1]=='delete':
            ocean_delete(get_topic(argv))

        elif argv[1]=='deploy':
            ocean_deploy ()

        elif argv[1]=='edit':
            ocean_edit(get_topic(argv))

        elif argv[1]=='getcode':
            ocean_get_code()

        elif argv[1]=='list':
            ocean_list(get_topic(argv))

        elif argv[1]=='path':
            print(ocean_path(get_topic(argv)))

        elif argv[1]=='pick':
            ocean_pick(get_topic(argv))

        elif argv[1]=='publish':
            ocean_publish()

        elif argv[1]=='show':
            ocean_show(get_topic(argv))

        elif argv[1]=='view':
            ocean_view(get_topic(argv))

        elif argv[1]=='web':
            ocean_web(get_topic(argv))

        else:
            print('No ocean command found, '+argv[1])
            ocean_help()
    else:
        print('No arguments given')
        ocean_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    ocean_command(argv)

