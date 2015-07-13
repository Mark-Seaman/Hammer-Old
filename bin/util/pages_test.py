#!/usr/bin/python
# Run a python script to test selenium

HEADLESS = True

from os import system, environ, chdir

pages = '''
google.com
shrinking-world.org
seamansguide.com
seamanslog.com
markseaman.org
app.eventthumper.com
Spiritual-Things.org/LifeApps
'''.split('\n')[1:-1]


# Start up Phantom JS to run a headless browser
def start_phantom_JS():
    if HEADLESS:
        system('rbg Xvfb :99 -ac>/dev/null')
        environ['DISPLAY'] = ":99"
        print 'Phantom JS DISPLAY on '#,environ['DISPLAY']


# Stop Phantom JS server to go back to normal
def stop_phantom_JS():
    if HEADLESS:
        system('killall Xvfb')
        print 'Phantom JS DISPLAY off'


 # The tester should only be run on certain computers.
def is_host_allowed():
    from platform   import node
    if 'seaman-' not in node():
        print 'This host can not run selenium,',node()
        return False
    else:
        return True


# Start Phantom JS and get all pages
def selenium_page_test():
    chdir (environ['pt'])
    if is_host_allowed():
        start_phantom_JS()
        from pages import test_web_pages
        test_web_pages(pages)
        stop_phantom_JS()


# Run the test as a program
if __name__=='__main__':
    selenium_page_test()
