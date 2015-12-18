'''
Tests for web code
-------------------

Run all of the tests for the 'web' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines
from switches import switches_get


def web_wiki_test():
    if switches_get("SHOW_WEB_PAGE"):
        return shell('web wiki')
    else:
        return 'Disabled web wiki page'


def web_wiki_test():
    if switches_get("SHOW_WEB_PAGE"):
        return shell('web issues')
    else:
        return 'Disabled web issues page'


def web_show_test():
    return shell('cat bin/web.py')
