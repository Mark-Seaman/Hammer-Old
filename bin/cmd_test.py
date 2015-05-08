'''
Command Tests
---------------

Run all of the tests for the 'cmd' objects.  Output the test results.

'''

from glob import glob
from os import listdir, environ, system
from os.path import join
from sys import argv

from tst import run_diff_checks, shell, lines, limit_lines


def cmd_add_test():
    '''Add and delete commands from the system'''
    return shell('cmd add-test xxx') + shell('cmd show xxx') + shell('cmd delete xxx')


def cmd_list_test():
    '''List the available commands'''
    return shell('cmd list') + shell('cmd show xxx')


def source_test():
    '''   List the source files from several directories   '''
    dirs = ['','bin','test']
    result = []
    for d in dirs:
        files = [f for f in glob(join(d,'*.py')) if '.pyc' not in f]
        result += sorted(files)
    return '\n'.join(result)+'\n'


def cmd_checker():
    my_tests = {
        'cmd-add': cmd_add_test,
        'cmd-list': cmd_list_test,
        'cmd-source': source_test,
    }
    run_diff_checks('cmd', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    cmd_checker()