#!/usr/bin/env python
# Wiki text formatter

from os.path    import isfile, exists
from sys        import argv, stdin
from re         import compile, IGNORECASE, DOTALL

# Create bold text if needed
def make_heading(line):
    tag = 'h1'  
    if line.startswith('** '):
        tag = 'h2'
    if line.startswith('*** '):
        tag = 'h3'
    if line.startswith('**** '):
        tag = 'h4'
    pat = compile(r"\*+ (.*)", IGNORECASE | DOTALL)
    return pat.sub(r'<h1>\1</h1>', line).replace('h1',tag)

# Create bold text if needed
def make_bold(line):
    pat = compile(r"\*\*(.*)\*\*", IGNORECASE | DOTALL)
    return pat.sub(r'<b>\1</b>', line)

# Create bold text if needed
def make_italic(line):
    pat = compile(r"\*([a-zA-Z0-9].*[a-zA-Z0-9])\*", IGNORECASE | DOTALL)
    return pat.sub(r'<i>\1</i>', line)

# Add paragraph breaks if needed
def break_paragraphs(line):
    if line=='': return '<br>'
    else: return line

# Remove the muse tag from the first line
def remove_muse(line):
    return line.replace ('-*-muse-*-', '').replace ('-*- muse -*-', '').rstrip()

# Preserve any four spaces together
def preserve_spaces(line):
    return line.replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;')

# Break lines for <space> at beginning
def space_breaks(line):
    always_break = False
    if always_break or (len(line)>0 and line[0]==' '):
        return  '<br/> '+line
    return line

# Add horizontal rules
def format_rules(line):
    i=line.find('---')
    if i!=-1:
       return line.replace('---', '<hr>')
    return line

# Add bullets
def format_bullets(line):
    i=line.find('  * ')
    if i!=-1:
        return "<ul><li>"+line[i+4:]+"</li></ul>"
    return line

# Format a RAW line, copied direct (for raw HTML for example) 	
def format_raw(line): 	
    i=line.find('  ::') 	
    if i!=-1: 	
        return line[i+4:] 	
    return line

# Convert the url in a string to an HTML anchor
def muse_double_anchor(url):
    s = r"\[\[([\/\w\.\:\-\_ \%]*)\]\[([ \w\.\-\_\,\?\%]*)\]\]"
    pat = compile(s, IGNORECASE | DOTALL)
    return pat.sub(r' <a href="\1">\2</a> ', url)

# Convert the url in a string to an HTML anchor
def muse_single_anchor(url):
    s = r"\[\[([\/\w\%\.\-\_]*)\]\]"
    pat = compile(s, IGNORECASE | DOTALL)
    return  pat.sub(r' <a href="\1">\1</a> ', url)

# Convert the url in a string to an HTML anchor
def muse_anchor(url):
    url = muse_double_anchor(url)
    return muse_single_anchor(url)

# Convert the url in a string to an HTML anchor
def url_to_anchor(url):
    s = r"(^|[\n ])(([\w]+?://[\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)"
    pat = compile(s, IGNORECASE | DOTALL)
    return pat.sub(r'\1<a href="\2" target="_blank">\2</a>', url)

# Convert the url in a string to an HTML image tag
def url_to_image(url):
    s = r"\[\[images/(([\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)\]\]"
    pat = compile(s, IGNORECASE | DOTALL)
    return pat.sub(r'<img src="/media/mybook/images/\1" alt="\1">', url)

# Convert the Wiki Words to hyperlinks
def wiki_words(text):
    s = r"([^A-Za-z\"\']*)([A-Z][a-z]+[A-Z][a-z]+([A-Z][a-z]+)*)([^A-Za-z\'\"]*)"
    pat = compile(s, DOTALL)
    return muse_anchor(pat.sub(r'\1[[\2]]\4', text))

# Convert a single line of muse to html
def convert_links(text1):
    text = text1
    text = format_raw(text)
    text = url_to_image(text)
    text = url_to_anchor(text)
    text = muse_anchor(text)
    return text

# Convert a single text line to html
def convert_line(line):
    line = line.decode('utf-8').encode('ascii', 'ignore')
    line = remove_muse(line).rstrip()
    line = space_breaks(line)
    line = format_rules(line)
    line = format_bullets(line)
    line = break_paragraphs(line)
    line = convert_links(line)
    line = preserve_spaces(line)
    line = make_heading(line)
    line = make_bold(line)
    return make_italic(line)

# Convert array of strings to html body text
def convert_html(text):
    text = map(convert_line, text)
    return '\n'.join(text)

# The first line holds the page title
def get_title(text):
    if len(text)>0: 
        return remove_muse(text[0]).rstrip()[2:][:-2]
    return 'No title'

# Turn a wiki word into a title, format the title with spaces to break each word.
def title_text(title):
    return title[0] + ''.join([ " "+c if c.isupper() else c  for c in title[1:] ])

# Convert from text block to HTML
def muse_to_html(text):
    return convert_html(text.split('\n'))