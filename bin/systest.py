from os import system
from re import sub
from sys import argv

from book_test import book_checker
from cmd_test import cmd_checker
from code_test import code_checker
from doc_test import doc_checker
from synch_test import synch_checker
from tst_test import tst_checker
from tst import run_diff_checks, shell, lines, limit_lines
from vc_test import vc_checker


def cmd_python_pip_test():
    '''Check the python setup for pip'''
    return shell('pip list')


def nose_test_execution():
    '''Run all nose tests  and report any changes'''
    system('nose 2> /tmp/nose; sleep 1')
    return sub(r'\d\.\d\d\ds', r'x.xxxs', shell('cat /tmp/nose'))


def process_status_test():
    '''Make sure that there are not too many processes running'''
    return limit_lines ('ps -e',190,230)


def pwd_test():
    '''List the current directory   '''
    return shell('pwd')


def system_test_list():
    '''Create a list of tests to manage'''
    return {
        #'nose': nose_test_execution,
        'vc': vc_checker,
        'cmd': cmd_checker,
        'book': book_checker,
        'doc': doc_checker,
        'tst': tst_checker,
        'pip': cmd_python_pip_test,
        'ps': process_status_test,
        'pwd': pwd_test,
        'synch': synch_checker,
        'code': code_checker,
    }


def system_checker():
    '''Execute all tests for the tst command'''
    my_tests = system_test_list()
    run_diff_checks('system', my_tests)


# Create a script that can be run from the shell
if __name__=='__main__':
    system_checker()
    