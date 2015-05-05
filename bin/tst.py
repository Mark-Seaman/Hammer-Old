#!/usr/bin/env python

from glob import glob
from os import system
from os.path import join
from subprocess import Popen,PIPE
from sys import argv
from re import sub

from diff_tests import execute_command, shell, lines, limit_lines
from cmd_test import cmd_python_pip_test, cmd_add_test, cmd_list_test


def nose_test_execution():
    '''
    Run nose over all the nose tests that are available. Report any changes.
    '''
    system('nose 2> /tmp/nose; sleep 1')
    return sub(r'\.\d\d\ds', r'.xxxs', shell('cat /tmp/nose'))


def process_status_test():
    '''
    Make sure that there are not too many processes running
    '''
    return limit_lines ('ps -e',10,250)


def pwd_test():
    '''
    List the current directory
    '''
    return shell('pwd')


def ls_test():
    '''
    List files in the current directory
    '''
    return shell('ls')


def source_test():
    '''
    List the source files from several directories
    '''
    dirs = ['','bin','test']
    result = []
    for d in dirs:
        files = [f for f in glob(join(d,'*.py')) if '.pyc' not in f]
        result += sorted(files)
    return '\n'.join(result)+'\n'


def count_source_lines_test():
    '''
    Count the lines of source code in the tst.py file
    '''
    return limit_lines ('cat bin/tst.py',80,120)


def like_test():
    '''
    Test the like switch to approve the correct answer
    '''
    system('''
        echo do not like this > test/dummy.correct
        tst like dummy > /dev/null
        ''')
    return ''
    

def dummy_test():
    '''
    Do nothing just to test the output commands
    '''
    return 'ok\n'


def output_test():
    '''
    Display the output from the last test run
    '''
    return shell('tst output cmd_add')


def vc_test():
    '''
    Test the vc command set
    '''
    return shell('vc test')


'''
Create a script that can be run from the tst
'''
if __name__=='__main__':

    my_tests = {
        'command-add': cmd_add_test,
        'commands': cmd_list_test,
        'dummy': dummy_test,
        'like': like_test,
        'lines': count_source_lines_test,
        'ls': ls_test,
        'nose': nose_test_execution,
        'output': output_test,
        'pip': cmd_python_pip_test,
        'ps': process_status_test,
        'pwd': pwd_test,
        'source': source_test,
        'vc': vc_test,
    }

    execute_command(argv, my_tests)
