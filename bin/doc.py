#!/usr/bin/env python

from os import system, listdir, environ, chdir, walk
from os.path import join, exists, isdir
from sys import argv



def doc_add(argv):
    ''' Create a new doc.'''
    d = doc_path(argv[2])
    print("New doc:"+d)
    system('echo "Document %s" > %s' % (d,d))


def doc_changes():
    '''Form the shell script for the commit command. '''
    command = 'cd $mb; git diff --word-diff'
    print('List all pending changes to the book')
    system(command)


def doc_status():
    '''Form the shell script for the commit command. '''
    command = 'cd $mb; git status'
    print('List all pending changes to the book')
    system(command)


def doc_commit(argv):
    '''Form the shell script for the commit command. '''
    if len(argv)>2:
        comment =  ' '.join(argv[2:])
    else:
        comment = 'Automatic book commit'
    command = '''cd $mb
        echo Commit all changes from the book project
        git add -A . &&
        git commit -m"%s" &&
        git pull &&
        git push
    ''' % comment
    system(command)


def doc_delete(argv):
    ''' Delete the doc.'''
    d = doc_path(argv[2])
    if not exists(d):
        print('doc delete: no file found, '+d)
    else:
        print('doc delete: '+d)
        system('rm '+d)


def doc_edit(argv):
    ''' Edit the content of a doc.'''
    d = doc_path(argv[2])
    print("edit:",d)
    system('e '+d)


def doc_help():
    '''Show all the doc docs and their usage.'''
    print('''
    usage: cmd doc [args]

    doc:

        add     [file]      # Add a new doc
        changes             # List doc changes 
        commit [message args] # Commit all changes to the book
        delete  [file]      # Delete a doc
        edit    [file]      # Edit the doc
        list    [file]      # List all docs
        path    [file]      # Show path to document
        show    [file]      # Show a doc
        status             # List doc changes 
        text                # Show markdown for all docs
      
            ''')


def doc_print_list(argv):
    '''List the parts of the doc source code.'''
    print("List the contents of this doc - "+doc_path(argv))
    directories = [d for d in listdir(doc_path(argv)) if isdir(doc_path([d]))]
    for d in directories:
        print(d+':')
        files = [join(d,f) for f in listdir(doc_path([d]))]
        print('    '+'\n    '.join(files))


def doc_find(argv):
    '''List the parts of the doc source code.'''
    root_dir = doc_path(argv)
    for root, dirnames, filenames in walk(root_dir):
        for filename in filenames:
            yield join(root, filename)


def doc_list(argv):
    '''List the parts of the doc source code.'''
    print("List the document contents")
    for f in doc_find(argv):
        print f.replace(doc_path()+'/','')


def doc_path(doc=None):
    '''Return the path name that corresponds to this document.'''
    path = join(environ['mybook'])
    if doc:
        return join(path,doc[0])
    else:
        return path


def doc_publish():
    '''Update all of the documents from the source'''
    pass
    # system('''# Build the HTML from markdown
    #     cd $mb/Hammer &&
    #     mkdocs build &&
    #     merge site ../website/Hammer
    #     server publish
    #     ''')

from tst import print_banner

def doc_show(argv):
    ''' Show the content of a doc.'''
    print("List the document contents")
    for f in doc_find(argv):
        print_banner (f.replace(doc_path()+'/',''))
        print (open(f).read())


def doc_web():  
    system('web http://mybookonline.org/static/book/Hammer')


def doc_command(argv):
    '''Execute all of the doc specific docs'''
    if len(argv)>1:

        if argv[1]=='add':
            doc_add(argv)

        elif argv[1]=='changes':
            doc_changes()

        elif argv[1]=='commit':
            doc_commit(argv)

        elif argv[1]=='delete':
            doc_delete(argv)

        elif argv[1]=='edit':
            doc_edit(argv)

        elif argv[1]=='list':
            doc_list(argv[2:])

        elif argv[1]=='path':
            print('path:'+doc_path(argv[2:]))

        elif argv[1]=='publish':
            doc_publish()

        elif argv[1]=='show':
            doc_show(argv[2:])

        elif argv[1]=='status':
            doc_status()

        elif argv[1]=='web':
            doc_web()

        else:
            print('No doc doc found, '+argv[1])
    else:
        doc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    doc_command(argv)