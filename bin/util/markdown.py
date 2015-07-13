#!/usr/bin/env python
# Edit the files from a Git Hub wiki as Muse docs

from os      import environ,listdir,system
from os.path import join,basename
from shutil  import copy
from re      import sub


#-----------------------------------------------------------------------------
# Replacer

# Replace one pattern with its substitute string
def replacer(replacements,text):
    results = []
    for line in text.split('\n'):
        for r in replacements:
            pattern,substitute = r
            line = sub(pattern,substitute,line)
            print "replacer: ",line
        results.append(line)
    return '\n'.join(results)


#-----------------------------------------------------------------------------
# From Markdown

# Apply a stack of substitutions
def map_markdown_to_muse(line):
    line = sub(r'^\* ', r' * ', line)
    line = sub(r'\*\*', r'**', line)
    line = sub(r'^# ',  '* ', line)
    line = sub(r'^## ', '** ', line)
    return line


# Convert a text block
def text_to_muse(text):
    text = map(map_markdown_to_muse, text.split('\n'))
    return '\n'.join(text)


# Convert one file to muse
def markdown_to_muse(f1,f2):
    title = basename(f1.replace('.md',''))
    title =  '* %s *     -*- muse -*-\n\n'%title
    text = open(f1).read().replace('\r','')
    text = text_to_muse(text)
    text = '\n'.join(text)
    open(f2,'wt').write(title+text)

    
# Convert the markdown files to muse
def convert_to_muse(d1,d2):
    for f in listdir(d1):
        if f.endswith('.md'):
            f1 = join(d1,f)
            f2 = join(d2,f.replace('.md',''))
            markdown_to_muse(f1,f2)
#-----------------------------------------------------------------------------
# To Markdown

# Convert one muse line
def map_muse_to_markdown(line):
    line = sub(r'^\* ', r'# ', line)
    line = sub(r'^\*\* ', r'## ', line)
    line = sub(r'^\s*\* ', r'* ', line)
    #line = sub(r'\[\[(LinkText)\]\]', r'\[\[\2\]\]', line)
    return line


# Convert a text block
def text_to_markdown(text):
    text = map(map_muse_to_markdown, text.split('\n'))
    return '\n'.join(text)


# Convert one file to markdown
def muse_to_markdown(f1,f2):
    text = open(f1).read().split('\n')[2:]
    text = text_to_markdown (text)
    open(f2,'wt').write('\r\n'.join(text))


# Convert muse files to markdown
def convert_to_markdown(d1,d2):
    for f in listdir(d1):
        f1 = join(d1,f)
        f2 = join(d2,f+'.md')
        muse_to_markdown(f1,f2)

