from random         import choice
from os.path        import dirname,join

from list           import split_lines,join_lines
from files          import list_files, read_text, do_command
from settings   import SCRIPTS_DIR


#-----------------------------------------------------------------------------
# PICK & QUOTE

# Get a directory of possible selection
def directory_listing(dir):
    return [ x for x in list_files(dir) if not x in ['Index','Random'] ]


# Insert a random selected file into this spot if requested
def lookup_file(dir, line):
    if '[[PICK]]' in line:
        pick = directory_listing(dir)
        pick = choice(pick)
        return 'selection:%s\n\n%s'%(pick,read_text(join(dir,pick)))
    return line


# Insert a random selected file into this spot if requested
def insert_random_text(dir,lines):
    return [ lookup_file(dir, l) for l in lines ]
    

# Feature a single line of the input stream
def lookup_quote(line, lines):
    if '[[QUOTE]]' in line:
        t = filter(lambda l:len(l)>4, lines[2:])
        t = filter(lambda l:not '**' in l, t)
        t = filter(lambda l:not '[[QUOTE]]' in l, t)
        return '<b>'+choice(t)+'</b><br>'
    return line


# Select a line of text to feature
def extract_random_line(lines):
    return [ lookup_quote(l, lines) for l in lines ]


#-----------------------------------------------------------------------------
# INCLUDE

# Replace a single include
def replace_include (dir,line):
    if '[[INCLUDE:' in line:
        filename = dir+'/'+line[10:-2]
        return read_text(filename)
    return line


# Map all of the include lines to their file replacements
def map_include_files(dir,lines):
    return  [ replace_include(dir,l) for l in lines ] 


#-----------------------------------------------------------------------------
# SCRIPT

# TODO: 
# Extract the command name to execute from a line of text
def command_name(doc):
    doc = doc.replace('..','x')
    doc = doc[9:-2]
    doc = doc.split('/')
    doc = '/'.join(doc[:1]) + ' ' + ' '.join(doc[1:])
    return join(SCRIPTS_DIR,doc)

# Replace a single include
def replace_scripts (line):
    if '[[SCRIPT:' in line:
        #print 'Execute (%s)'%command_name(line)
        return do_command(command_name(line))
    return line

# Map all of the include lines to their file replacements
def map_scripts(lines):
    return  [ replace_scripts(l) for l in lines ] 


#-----------------------------------------------------------------------------
# LINES & PRE

# Add paragraph breaks if needed
def break_paragraphs(line):
    if line=='': return '</p><p>'
    else: return line

# Replace a single include
def break_lines (lines):
    result = []
    add_break = False
    for l in lines:

        if add_break:
            if l[:2] == ']]':
                add_break = False
                continue
        else:
            if '[[LINES' in l:
                add_break = True
                continue

        if add_break:
            result.append(break_paragraphs(l)+'<br/>')
        else:
            result.append(l)

    return result

# Replace a single include
def preformated_lines (lines):
    result = []
    add_pre = False
    for l in lines:
        if not add_pre and  '[[PRE' in l:
            add_pre = True
            result.append('<pre>')
            continue
        if add_pre and l[:2] == ']]':
            add_pre = False
            result.append('</pre>')
            continue
        result.append(l)
    return result

#-----------------------------------------------------------------------------
# TABLE

def format_row(row):
    return '<td>' + '</td><td>'.join(row.split(',')) + '</td>\n'

# Format the HTML for the table
def format_table(lines):
    x = '<tr>\n'
    y = [ format_row(row) for row in lines ]
    z = '</tr>\n'
    return x+''.join(y)+z

# Include an embedded table
def insert_table (lines):
    result = []
    table = []
    add_pre = False
    for l in lines:
        if not add_pre and  '[[TABLE' in l:
            add_pre = True
            result.append('<table>')
            continue
        if add_pre and l[:2] == ']]':
            add_pre = False
            result.append(format_table(table))
            result.append('</table>')
            continue

        if add_pre:
            table.append(l)
        else:
            result.append(l)
    return result


#-----------------------------------------------------------------------------

# Format this text as a page with embedded widgets
def format_widgets(filename, text):
    dir = dirname(filename)
    lines = split_lines(text)
    lines = map_include_files(dir,lines)
    lines = split_lines(join_lines(lines))
    lines = insert_table (lines)
    lines = preformated_lines(lines)
    lines = break_lines(lines)
    lines = insert_random_text(dir,lines)
    lines = extract_random_line(lines)
    lines = map_scripts(lines)
    return join_lines(lines)

