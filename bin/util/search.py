# Search utilities

from os import system

from files import write_file, do_command,recursive_list


#-----------------------------------------------------------------------------
# Count lines

# Show the line count
def count_lines(text, label=None):
    if label:
        print label % len(text.split('\n'))
    else:       
        print 'Found ',len(text.split('\n')), 'lines'

# Verify the expected number of lines
def check_lines(text, min, max, label=None):
    n = len(text.split('\n'))
    if n<min or n>max:
        count_lines(text, label=None)


#-----------------------------------------------------------------------------
# Find

# Time by time if needed
def time_filter(files,time):
    num = len(files)/10
    if time=='new':
        return files[num:]
    if time=='old':
        return files[:num]


# Include these directories of files
def include_files(include):
    results = []
    for i in include:
        for f in recursive_list(i):
            results.append( i+'/'+f)
    return results


# Match a list of file
def find (include=None, exclude=None, time=None):
    files = include_files(include.split('\n'))
    if time:
        files = time_filter(files,time)
    if exclude:
        files = exclude_files(files,exclude)
    return '\n'.join(files)


#-----------------------------------------------------------------------------
# Search

# Search for strings in files
def search (files,include,exclude=None):
    files   = files.split('\n')
    include = include.split('\n')
    write_file("/tmp/xfiles",files)
    write_file("/tmp/xinclude",include)
    if exclude:
        exclude = exclude.split('\n')
        write_file("/tmp/xexclude",exclude)
        return do_command ('match /tmp/xfiles /tmp/xinclude /tmp/xexclude')
    else:
        return do_command ('match /tmp/xfiles /tmp/xinclude')
        
#-----------------------------------------------------------------------------
# Replace

# Substitute all matches within file list
def replace (files, patterns):
    #files   = files.split('\n')
    patterns = [ r.split('|-|') for r in patterns.split('\n') ]
    print patterns
    for p in patterns:
        s = search (files, p[0])
        print s.split(':')[0], ':',p[0]


