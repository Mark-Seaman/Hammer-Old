#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from text_test import text_checker
from book import book_read_index


def text_convert_to_outline(topic):
    '''Convert headings to outline indents'''
    print('Outline: '+topic)
    topics = join(environ['book'],'outline',topic+'.md')
    text = open(topics).read().split('\n')
    text = [t.replace('### ','            ') for t in text]
    text = [t.replace('## ','        ') for t in text]
    text = [t.replace('# ','    ') for t in text]
    text = '\n'.join(text)
    return text


def text_outline():
    '''Build a new outline from the book text'''
    results = "Outline of this book\n"
    for topic in book_read_index('Chapters'):
        results += text_convert_to_outline(topic)+'\n\n'
    outline_file = join(environ['book'],'Outline.outline')
    with open(outline_file,'w') as f:
        f.write(results+'\n')
    #system('e $book/Outline.outline')
    return results


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


def text_headings():
    '''Build a new outline from the book text'''
    results = "Outline of this book\n"
    for topic in book_read_index('Chapters'):
        text = extract_headings(topic)
        results += text+'\n\n\\newpage\n'
    outline_file = join(environ['book'],'Outline.md')
    with open(outline_file,'w') as f:
        f.write(results+'\n')
    #system('e $book/Outline.md')
    return results


def text_help():
    '''Show all the text texts and their usage.'''
    print('''
    usage:  text cmd [args]

    text:

        index     [file] -- Convert from outline to markdown
        headings  [file] -- Extract headings from text content
        outline   [file] -- Convert from markdown to outline
        show      [file] -- Show the text
        test             -- Self test
      
            ''')


def text_show(chapter):
    '''Show the content of a text.'''
    print("text:",argv[2])
    f = join(environ['book'], 'chapters', '%s.md'%chapter)
    print(open(f).read())


def text_command(argv):
    '''Execute all of the text specific texts'''
    if len(argv)>1:

        if argv[1]=='index':
            text_index(argv)

        elif argv[1]=='headings':
            text_headings()

        elif argv[1]=='outline':
            text_outline()

        elif argv[1]=='show' and len(argv)>2:
            text_show(argv[2])

        elif argv[1]=='test':
            text_checker()

        else:
            print('No text command found, '+argv[1])
            text_help()
    else:
        print('No arguments given')
        text_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    text_command(argv)