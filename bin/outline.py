#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from outline_test import outline_checker
from book import book_read_index
from tst import shell


#-------------------------------
# outline differences


def outline_diff(files):
    system('outline index > /dev/null')
    system('outline headings > /dev/null')
    if not files:
        files = book_read_index('Chapters')
    for topic in files:
        system('''
            echo '---------------------------------------------------------'
            echo '                      %s'
            echo '---------------------------------------------------------'
            diff -b $book/outline/%s.md $book/content/%s.md
            ''' % (topic,topic,topic))


#-------------------------------
# content directory

def convert_to_headings(topic):
    '''Convert the content outline to markdown'''
    print('Build the text index of headings from an outline '+topic)
    input_file   = join(environ['book'], 'content', topic+'.outline')
    outline_file = join(environ['book'], 'content', topic+'.md')
    text = open(input_file).read().split('\n')
    text = [t for t in text if t.strip()]
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

def extract_headings(topic):
    '''Extract the outline from chapter file to make outline file'''
    print('Outline: '+topic)
    chapter_dir = join(environ['book'],'chapters')
    outline_dir = join(environ['book'],'outline')
    path1 = join(chapter_dir,topic+'.md')
    path2 = join(outline_dir,topic+'.md')
    text = [t for t in open(path1).read().split('\n') if t.startswith('#')]
    text = '\n'.join(text)
    with open(path2,'w') as f:
        f.write(text+'\n')
    return text


def outline_headings():
    '''Build a new outline from the book text'''
    results = "Outline of this book\n"
    for topic in book_read_index('Chapters'):
        text = extract_headings(topic)
        results += text+'\n\n\\newpage\n'
    outline_file = join(environ['book'],'Outline.md')
    with open(outline_file,'w') as f:
        f.write(results+'\n')
    return results


#-------------------------------
# outline command processing


def outline_help():
    '''Show all the outline outlines and their usage.'''
    print('''
    usage:  outline cmd [args]

    outline:

        index     [file] -- Convert from outline to markdown
        headings  [file] -- Extract headings from outline content
        outline   [file] -- Convert from markdown to outline
        diff      [file] -- Find the differences in the outlines
        show      [file] -- Show the outline
        test             -- Self test
      
            ''')


def outline_show(chapter):
    '''Show the content of a outline.'''
    print("outline:"+chapter)
    f = join(environ['book'], '%s'%chapter)
    print(open(f).read())


def outline_command(argv):
    '''Execute all of the outline specific outlines'''
    if len(argv)>1:

        if argv[1]=='index':
            outline_index()

        elif argv[1]=='headings':
            outline_headings()

        elif argv[1]=='outline':
            outline_outline()

        elif argv[1]=='diff':
            outline_diff(argv[2:])

        elif argv[1]=='show' and len(argv)>2:
            outline_show(argv[2])

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