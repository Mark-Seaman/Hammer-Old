#!/usr/bin/python
# Show the index file

from sys     import argv
from os.path import exists
from os      import system

class Index:
    filename = 'AnalysisJournal'
    text = ''
    node = 0

# Context for index location (file, text, node)
index = Index()
def set_file(filename):
    index.filename = filename
def set_text(text):
    index.text = text
def set_node(node):
    index.node = node

# Read index file
def read_index(filename):
    set_file(filename)
    return open(filename).read().split('\n')

# Read index file
def refresh_index():
    return open(index.filename).read().split('\n')

# Count the leading spaces
def num_spaces(line):
    return len(line) - len(line.lstrip())

# Return the indent level
def indent_level(text,i):
    return num_spaces(text[i])

# Check for a child
def is_child(text,level):
    if len(text)==0: return False
    return indent_level(text,0) > level

# Weight of all children below this node
def count_children(text,i):
    level = indent_level(text,i)
    start = i+1
    if not is_child(text[start:start+1],level): return 0
    level =  indent_level(text,start) 
    for j,line in enumerate(text[start:]):
        if num_spaces(line) < level: return j
    return len(text)-i

# Get the list of child nodes
def list_children(text,i):
    level = indent_level(text,i)
    start = i+1
    if not is_child(text[start:start+1],level): return []
    level =  indent_level(text,start) 
    result = []
    for i,line in enumerate(text[start:]):
        if num_spaces(line) < level: return result
        if num_spaces(line) == level and len(line.strip())>0:
            result.append(i+start)
    return result

# Return the index of the parent
def parent_node(text,i):
    level = indent_level(text,i)
    for j in range(i):
        #print 'check', i, i-j
        if level > indent_level(text,i-j-1):return i-j-1
    return i

# Remove link brackets
def remove_muse(line):
    return line.replace ('-*-muse-*-','')

# Remove link brackets
def remove_brackets(line):
    return line.replace ('[[','').replace(']]','')

# Show any brain topics
def brain_topic(line):
    f = line
    f = remove_brackets(f)
    f = remove_muse(f)
    f = "/home/seaman/Documents/Brain/"+f.strip()
    if exists(f): return f 

# Edit the topic for this line of text
def edit_brain_topic (text,node):
    f = brain_topic(text[node])
    if not f:
        print 'Brain topic not found for: %s' % f
    else:
        print '"%s"' % f.strip(), f.strip().find('Fly')
        if f.find('Fly')!=-1:
            text,node = fly_brain_topic(text,node)
        else:
            system ('e %s' % f)
    return (text,node)

# Fly the topic for this line of text
def fly_brain_topic (text,node):
    line = text[node]
    f = brain_topic(line)
    if not f:
        print 'Brain topic not found for: %s' % line
    else:
        print 'Open fly file', f
        text = read_index(f)
        node = goto_node(text,0,0)
    return (text,node)
    
# Edit a specific line in the index file
def edit_index(line):
    system ('e %s:%d' % (index.filename,line))

# Show any brain topics
def brain_topic_string (text,i):
    if brain_topic(text[i]): return ' * '
    return ''

# Show the count for the children
def count_string (text,i):
    children = count_children(text,i)
    if children>1: return '  (%d)'%count_children(text,i)
    return ''

# Format a single entry    
def print_line (num,line,file,count):
        if num!=0: print str(num)+'. ', 
        print '%-20s'%remove_brackets(remove_muse(line)).strip(), file, count

# Display text for a list of nodes
def display_text(text, nodes):
    n = 0
    for i in nodes:
        print_line(n,text[i], brain_topic_string(text,i), count_string(text,i))
        n+=1

# Show one node and its children
def display(text,i):
    display_text(text,  [i] + list_children(text,i))
    print

# Walk the tree to find the parent
def goto_parent(text, i):
    i = parent_node(text,i)
    display(text,i)
    return i

# Go to the child node and display the text
def goto_child(text, i, j):
    children = list_children(text,i)
    #print children
    if len(children) > j:
        return children[j]
    else:
        return i

# Switch to either parent or child node
def goto_node(text, node,command):
    if command == 0:
        node = parent_node(text,node)
        #print 'Parent = ', node
    else:
        node = goto_child(text, node, command-1)
        #print 'Child', command, '=', node
        #if count_children(text,node)==0:
        #    text,node = edit_brain_topic(text,node)
    display(text, node)
    return node
