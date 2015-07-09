
from datetime   import datetime
from os         import system,chdir,getcwd
from os.path    import isfile, isdir, exists, join
from re         import compile, IGNORECASE, DOTALL

from wiki  import *
from tabs  import format_tabs, format_doc
from files import read_input, read_text, write_file, is_writable
from domain import domain_directory
from log    import append_log
from settings import DOC_ROOT


# Log the document hits
def log_page(doc):
    append_log(doc,'docs')


# Convert a url to a directory
def doc_path(host,user,path):
    dir = domain_directory(host)
    user = user.replace('Anonymous', 'Public')
    if dir: 
        doc = user+'/'+dir+'/'+path
    else:
        doc = user+'/'+path
    log_page('path '+doc)
    return join(DOC_ROOT,doc)


# Return the redirect page (after looking for Public & Private doc)
def page_redirect (host,user,path,allow_public=True):

    log_page('redirect '+host+' '+user+' '+path+' '+str(allow_public))

    if allow_public:
        doc = doc_path(host,'Public',path)
        index = join(doc,'Index')
        if exists(doc) and isfile(doc):
            return
        if exists(doc) and isdir(doc) and exists(index):
            return path+'/Index'
       
    doc = doc_path(host,user,path)
    index = join(doc,'Index')
    if exists(doc) and isfile(doc):
        return
    if exists(doc) and isdir(doc) and exists(index):
        return path+'/Index'
    if exists(doc) and isdir(doc) and not exists(index):
        return  path+'/Index/missing'
    return path + '/missing' 

 
# Determine if editing is allowed
def allow_edit(host,user,path):
    return exists(doc_path(host,user,path))


# If editing is allowed then make a hyperlink
def edit_link(host,user,path):
    if allow_edit(host,user,path):
        return '<a href="http://'+host+'/'+path+'/edit">Edit Document</a>'
    else:
        return ''


# Format the doc contents into HTML
def show_page(host,user,path,allow_public=True):
    log_page('show '+host+' '+user+' '+path)
    if allow_public:
        doc = doc_path(host,'Public',path)
        if exists(doc):
            return format_doc(doc)

    doc = doc_path(host,user,path)
    if exists(doc):
        return edit_link(host,user,path)+format_doc(doc)        


# Put the document text in storage
def put_page(host,user,path,text=None):
    log_page('put '+host+' '+user+' '+path)
    if text:
        write_file(doc_path(host,user,path), text.split('\n'))
    else:
        write_file(doc_path(host,user,path), read_input())


# Get the document text from storage
def get_page(host,user,path):
    log_page('get '+host+' '+user+' '+path)
    return read_text(doc_path(host,user,path))

