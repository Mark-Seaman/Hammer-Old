#!/usr/bin/env python
# Find the files that match a criteria

from os      import remove, path, getcwd, system, listdir, mkdir, walk, access, W_OK
from sys     import argv
from os.path import isfile, getmtime, join
from glob    import glob


# Recursive list
def recursive_list(d):
    matches = []
    for root, dirnames, filenames in walk(d):
        for filename in filenames:
            matches.append(join(root, filename))
    return matches


# List the files within a directory
def list_files(d):
    return filter(isfile, glob(d + "/*"))


# Get a file list sorted by time (recent last)
def time_sort_files(d,files):
    files.sort(key=lambda x: getmtime(x))
    return files


# Oldest 10% of the files
def oldest(files):
    if len(files)==0: return files
    return files[:len(files)/10]


# Newest 10% of the files
def newest(files):
    if len(files)==0: return files
    return files[-len(files)/10:]


# Print the list of selected files 
def print_files(label, files, select=None):
    if select:
        files = select(files)
    print label+':\n  ', '\n   '.join(files)


def list_directory(directory,select):
    #files = list_files(d)
    files = recursive_list(d)
    files = time_sort_files(d,files)

    if select=='old':
        print_files('Old Files', files, oldest)
    if select=='new':
        print_files('New Files', files, newest)
    if select=='all':
        print_files('All Files',    files)


# Sort the files by time
d='.'
select = 'all'
if len(argv)>1:
    d = argv[1]
if len(argv)>2:
    select = argv[2]
list_directory(d,select)
