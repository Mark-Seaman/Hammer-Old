#!/usr/bin/env python
# Run a python script to test support center web pages

from os.path  import join,exists
from os import system,chdir,mkdir,environ
from platform import node
from subprocess import Popen,PIPE
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from socket   import gethostname

from store import save, recall, expire, expiration
from diff  import diff_string
from files import write_file

# Global vars
accept_all_pages = False


# Get Support Center page
def get_page_text(browser,page):
    try:
        browser.get('http://'+page)
        body = browser.find_element_by_tag_name('body')
        text = body.text.decode('ascii','ignore')
    except:
        text = 'File not found: '+page
        text = '\n\nTitle:%s\n%s\n' % (browser.title, text )
    return text.replace('localhost:8054','shrinking-world.org')


# Login to the Support Center web site
def login(browser,page):
    get_page_text(browser,page)
    from local_settings import username,password
    username_field = browser.find_element_by_name('username')
    username_field.send_keys(username)
    password_field = browser.find_element_by_name('password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)


#----------------------------------------------------------------------------
# Page tracker in Redis


# Print the text from a Support Center page
def print_page_text(browser,page):
    print text(url)

# Return the output from the last run
def page_text(url):
    return recall(url+'.txt')


# Return the output from the last run
def page_html(url):
    return recall(url+'.html')
  
  
# Lookup the correct output for the test
def page_correct(url):
    correct_text = recall(url+'.correct')
    if correct_text:
        write_file(join(environ['pt'],gethostname(),url), [correct_text])
    return correct_text


# Accept these test results        
def like(url):
    text = recall(url+'.txt')
    save(url+'.correct', text)


# Calculate the difference from what was expected
def page_diff(url):
    t1 = page_text(url)
    t2 = page_correct(url)
    if not t2:
        save(url+'.correct',t1)
        t2 = t1
    if t1!=t2:
        print '\n_____________________________________________________\n'
        print 'FAIL:  %-35s'%url, len(t1), len(t2)
        print '_____________________________________________________'

        print diff_string(t1,t2)
        return True
    else:
        return False


#----------------------------------------------------------------------------
# Page files


# Get the web page, extract the text, and save the file
def save_page_text(browser,page):
    text = get_page_text(browser,page)
    save(page+'.txt', text)
    page_diff(page)
    #print 'page: %s\ntext:\n%s\n\n'%(page,page_text(page))


# Test a single page from the requested host
def test_web_page(browser,page):
    #print 'Testing', page, '...'
    if page=='http://login':
        login(browser,'login')
        print 'Login done'
        return 
    save_page_text(browser,page)


# Get the home page, Login, Read all pages
def test_web_pages(pages):

    #browser = webdriver.Chrome()
    browser = webdriver.Firefox()

    print 'TESTING...'
    #exit(0)
    #try:
    for page in pages:
        print 'get page:',page
        test_web_page(browser,page)
    #except:
    #    print 'Test web pages failed'

    browser.quit()
