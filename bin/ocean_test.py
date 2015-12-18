'''
Tests for ocean code
-------------------

Run all of the tests for the 'ocean' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from shell import shell, lines, limit_lines
from switches import switches_get


def ocean_help_test():
    return shell('ocean') + '\n' + shell('ocean help')


def ocean_path_test():
    return shell('ocean path')


def ocean_web_test():
    if switches_get('SHOW_WEB_PAGE'):
        return shell('ocean web static')
    else:
        return 'Web page display is disabled.  Change $SHOW_WEB_PAGE to show.'

