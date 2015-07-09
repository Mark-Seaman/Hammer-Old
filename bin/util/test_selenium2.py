#!/usr/bin/python
# Run a python script to test selenium


def selenium_install_test():

    from selenium import webdriver
    
    browser = webdriver.Firefox()
    #browser = webdriver.Chrome()
    
    browser.get('http://google.com')
    print browser.title
    browser.quit()
