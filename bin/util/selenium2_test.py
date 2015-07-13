#!/usr/bin/python
# Run a python script to test selenium


def selenium_install_test():

    try:
        print 'Run selenium_install_test()'
        from selenium import webdriver
    
        browser = webdriver.Firefox()
        #browser = webdriver.Chrome()
    
        browser.get('http://google.com')
        print browser.title
        browser.quit()

    except:
        print 'Error: No selenium installed'
 

selenium_install_test()
