#!/usr/bin/env python

import unittest

try:
    from selenium import webdriver

    class TestGoogleHomepage(unittest.TestCase):
    
        def setUp(self):
            self.browser = webdriver.Firefox()
        
            def testTitle(self):
                self.browser.get('http://google.com/')
                self.assertIn(u'Google', self.browser.title)
        
            def tearDown(self):
                self.browser.quit()

except:
    print "Error: No selenium is installed"

    

if __name__ == '__main__':
    unittest.main(verbosity=2)
