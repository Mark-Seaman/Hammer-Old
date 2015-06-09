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


def outline_content(files=None):
    if not files:
        files = book_read_index('Chapters')
        outline_write_content(1, files, content_filename(1))
        outline_write_content(2, files, content_filename(2))
        outline_write_content(3, files, content_filename(3))
    else:
        outline_write_content(3, files)


#-------------------------------
# outline differences

def outline_diff(files):
    system('outline index > /dev/null')
    system('outline headings > /dev/null')
    if not files:
        files = book_read_index('Chapters')
    for topic in files:
        print('Diff: '+topic)
        cmd = 'diff -B $book/outline/%s.outline $book/content/%s.outline > $book/outline/%s.diff'
        system(cmd % (topic,topic,topic))
    path1 = join(environ['book'],'outline','%s.diff')
    path2 = join(environ['book'],'outline','Outline.diff')
    join_files(path1, path2)


#-------------------------------
# content directory

def convert_to_headings(topic):
    '''Convert the content outline to markdown'''
    print('Build the text index of headings from an outline '+topic)
    input_file   = join(environ['book'], 'content', topic+'.outline')
    outline_file = join(environ['book'], 'content', topic+'.md')
    text = open(input_file).read().split('\n')
    text = [t for t in text if t.strip()]
    text = [t.replace('                ','#### ') for t in text]
    text = [t.replace('            ','### ') for t in text]
    text = [t.replace('        ','## ') for t in text]
    text = [t.replace('    ','# ') for t in text]
    text = '\n'.join(text)
    print(text)
    with open(outline_file,'w') as f:
        f.write(text+'\n')


def outline_index():
    '''Convert the content outline to markdown'''
    print('Build the text index of headings from content outline')
    convert_to_headings('Outline')
    for topic in book_read_index('Chapters'):
        convert_to_headings(topic)
    

#-------------------------------
# outline directory

def outline_convert_to_outline(topic):
    '''Convert headings to outline indents'''
    print('Outline: '+topic)
    topics = join(environ['book'],'outline',topic+'.md')
    text = open(topics).read().split('\n')
    text = [t.replace('#### ','                ') for t in text]
    text = [t.replace('### ','            ') for t in text]
    text = [t.replace('## ','        ') for t in text]
    text = [t.replace('# ','    ') for t in text]
    text = '\n'.join(text)
    return text


def outline_outline():
    '''Build a new outline from the book text'''
    results = "Outline of this book\n"
    for topic in book_read_index('Chapters'):
        results += outline_convert_to_outline(topic)+'\n\n'
    outline_file = join(environ['book'],'Outline.outline')
    with open(outline_file,'w') as f:
        f.write(results+'\n')
    return results


#-------------------------------
# chapters directory

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


def convert_to_outline(headings):
    '''Extract the outline from chapter file to make outline file'''
    text = [t for t in headings.split('\n') if t.startswith('#')]
    text = [t.replace('#### ','                ') for t in text]
    text = [t.replace('### ','            ') for t in text]
    text = [t.replace('## ','        ') for t in text]
    text = [t.replace('# ','    ') for t in text]
    return '\n'.join(text)


def extract_headings(topic):
    '''Extract the outline from chapter file to make outline file'''
    chapter_dir = join(environ['book'],'chapters')
    outline_dir = join(environ['book'],'outline')
    path1 = join(chapter_dir,topic+'.md')
    path2 = join(outline_dir,topic+'.md')
    text = [t for t in open(path1).read().split('\n') if t.startswith('#')]
    text = '\n'.join(text)
    return text


def book_outline():
    '''Build a new outline from the book text'''
    results = "Outline of this book\n"
    for topic in book_read_index('Chapters'):
        text = read_outline_fragment(topic)
        results += text+'\n\n\\newpage\n'
        save_outline ()
    outline_file = join(environ['book'],'outline','Outline.outline')
    with open(outline_file,'w') as f:
        f.write(results+'\n')
    return results


def save_headings(directory, topic, text):
   with open(path2,'w') as f:
        f.write(text+'\n')


def save_outline(directory, topic, headings):
    path = join(environ['book'], directory, topic+'.outline')
    outline = convert_to_outline(headings)
    with open(path,'w') as f:
        f.write(outline+'\n')


def outline_edit(chapter=None):
    update_outline_files()
    if chapter:
        system('e '+join(environ['book'],'content','%s.outline' % chapter[0]))
        system('e '+join(environ['book'],'outline','%s.outline' % chapter[0]))
    else:
        system('e '+join(environ['book'],'content','Outline.outline'))
        system('e '+join(environ['book'],'outline','Outline.outline'))
 

#-------------------------------
# outline command processing


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


def outline_show(chapter=None):
    '''Show the content of a outline.'''
    update_outline_files()
    path1 = join(environ['book'],'content','%s.outline')
    path2 = join(environ['book'],'content','Outline.outline')
    join_files(path1, path2)


def update_outline_files():
    '''Build a new outline from the book text'''
    results = "Outline of this book\n"
    for topic in book_read_index('Chapters'):
        text = read_chapter(topic)
        text = extract_headings(text)
        save_headings('outline', topic, text)
        save_outline('outline', topic,text)

    path1 = join(environ['book'],'outline','%s.md')
    path2 = join(environ['book'],'outline','Outline.md')
    join_files(path1, path2)


def outline_command(argv):
    '''Execute all of the outline specific outlines'''
    if len(argv)>1:

        if argv[1]=='book':
            book_outline()

        elif argv[1]=='content':
            outline_content(argv[2:])

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