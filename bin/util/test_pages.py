#!/usr/bin/python
# Run a python script to test selenium


pages = '''
google.com
shrinking-world.org
markseaman.org
appthumper.com
Spiritual-Things.org/LifeApps
'''.split('\n')[1:-1]


def selenium_page_test():
    from os         import environ, chdir
    from platform   import node
        
    chdir (environ['pt'])

    # The tester should only be run on seaman computers.
    if 'seaman-' not in node():
        print 'This host can not run selenium,',node()
    else:
        from util.pages import test_web_pages
        test_web_pages(pages)
