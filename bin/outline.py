#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from outline_test import outline_checker
from book import book_read_index
from tst import shell


#-------------------------------
# outline contents

def heading_string(topic):
    return '\n\n%s\n%s\n%s\n\n' % ('-'*60, ' '*20+topic, '-'*60)


def assemble_files(input_path,output_path):
    '''Create an agregate file by concatenating other files'''
    with open(output_path,'w') as f:
        for topic in book_read_index('Chapters'):
            text = heading_string(topic) + open(input_path % topic).read()
            f.write(text+'\n')


def join_files(path1,path2):
    '''Create a file and list the contents'''
    assemble_files(path1, path2)
    print(open(path2).read())


def content_filename(depth):
    '''Form the file name for the contents of a certain depth'''
    return join(environ['book'],'content','Content-%d.outline' % depth)


#-------------------------------
# converters 

def outline_content(files=None):

    def outline_write_content(depth, files, content_file=None):
        '''Write the outline for this chapter'''
        if content_file:
            open(content_file, 'w').close()
        for topic in files:
            filename = join(environ['book'],'content','%s.outline' % topic)
            text = open(filename).read().split('\n')
            text = [t for t in text if not t.startswith('    '*(1+depth)) and t.strip()]
            text = '\n'.join(text)
            if content_file:
                with open(content_file,'a') as f:
                    f.write(heading_string(topic)+text+'\n')
            else:
                print(heading_string(topic)+text)

    if not files:
        files = book_read_index('Chapters')
        outline_write_content(1, files, content_filename(1))
        outline_write_content(2, files, content_filename(2))
        outline_write_content(3, files, content_filename(3))
    else:
        outline_write_content(3, files)


def convert_to_headings(text):
    '''Convert the content outline to markdown'''
    #print('Build the text index of headings from an outline ')
    text = text.split('\n')
    text = [t for t in text if t.strip()]
    text = [t.replace('                ','#### ') for t in text]
    text = [t.replace('            ','### ') for t in text]
    text = [t.replace('        ','## ') for t in text]
    text = [t.replace('    ','# ') for t in text]
    return '\n'.join(text)
    

def convert_to_outline(headings):
    '''Extract the outline from chapter file to make outline file'''
    text = [t for t in headings.split('\n') if t.startswith('#')]
    text = [t.replace('#### ','                ') for t in text]
    text = [t.replace('### ','            ') for t in text]
    text = [t.replace('## ','        ') for t in text]
    text = [t.replace('# ','    ') for t in text]
    return '\n'.join(text)


def extract_headings(text):
    '''Extract the outline from chapter file to make outline file'''
    text = [t for t in text.split('\n') if t.startswith('#')]
    return '\n'.join(text)


#--------------------------------
# Files

def outline_edit(chapter=None):
    update_outline_files()
    if chapter:
        system('e '+join(environ['book'],'content','%s.outline' % chapter[0]))
        system('e '+join(environ['book'],'outline','%s.outline' % chapter[0]))
    else:
        system('e '+join(environ['book'],'content','Outline.outline'))
        system('e '+join(environ['book'],'outline','Outline.outline'))
 

def outline_show(chapter=None):
    '''Show the content of a outline.'''
    update_outline_files()
    path = join(environ['book'],'content','Content-3.outline')


def read_chapter(topic):
    '''Read chapter text'''
    chapter_dir = join(environ['book'],'chapters')
    path = join(chapter_dir,topic+'.md')
    return open(path).read()


def read_outline(topic):
    '''Read hand written outline content text'''
    chapter_dir = join(environ['book'],'content')
    path = join(chapter_dir,topic+'.outline')
    return open(path).read()


def save_headings(directory, topic, text):
   with open(join(environ['book'], directory, topic+'.md'), 'w') as f:
        f.write(text+'\n')


def save_outline(directory, topic, headings):
    path = join(environ['book'], directory, topic+'.outline')
    outline = convert_to_outline(headings)
    with open(path,'w') as f:
        f.write(outline+'\n')


def outline_diff(files):
    update_outline_files()
    for topic in book_read_index('Chapters'):
        cmd = 'diff -B $book/outline/%s.outline $book/content/%s.outline > $book/outline/%s.diff'
        system(cmd % (topic,topic,topic))
    path1 = join(environ['book'],'outline','%s.diff')
    path2 = join(environ['book'],'outline','Outline.diff')
    join_files(path1, path2)
    system('rm $book/outline/*.diff')


def update_outline_files():
    '''Build a new outline from the book text'''
    results = "Outline of this book\n"
    for topic in book_read_index('Chapters'):

        print('Outline: '+topic)
        text = extract_headings(read_chapter(topic))
        save_headings('outline', topic, text)
        save_outline('outline', topic, text)
        text = convert_to_headings(read_outline(topic))
        save_headings('content', topic, text)

    path1 = join(environ['book'],'outline','%s.md')
    path2 = join(environ['book'],'outline','Outline.md')
    assemble_files(path1, path2)
    outline_content()
   

def outline_help():
    '''Show all the outline outlines and their usage.'''
    print('''
    usage:  outline cmd [args]

    outline:

        book             -- Extract an outline from the chapter text
        content   [file] -- Show the table of contents
        edit      [file] -- Edit the nested outlines for the book
        headings  [file] -- Extract headings from outline content
        outline   [file] -- Convert from markdown to outline
        diff      [file] -- Find the differences in the outlines 
        show      [file] -- Show the outline
        test             -- Self test
      
            ''')

def outline_command(argv):
    '''Execute all of the outline specific outlines'''
    if len(argv)>1:

        # if argv[1]=='book':
        #     book_outline()

        if argv[1]=='content':
            update_outline_files()

        elif argv[1]=='edit':
            outline_edit(argv[2:])

        elif argv[1]=='diff':
            outline_diff(argv[2:])

        elif argv[1]=='show':
            outline_show(argv[2:])

        elif argv[1]=='test':
            outline_checker()

        else:
            print('No outline command found, '+argv[1])
            outline_help()
    else:
        print('No arguments given')
        outline_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    outline_command(argv)