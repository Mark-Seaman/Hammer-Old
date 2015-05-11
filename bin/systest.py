from os import system
from re import sub
from sys import argv

from book_test import book_checker
from cmd_test import cmd_checker
from doc_test import doc_checker
from vc_test import vc_checker
from tst_test import tst_checker
from tst import run_diff_checks, shell, lines, limit_lines


def cmd_python_pip_test():
    '''Check the python setup for pip'''
    return shell('pip list')


def nose_test_execution():
    '''Run all nose tests  and report any changes'''
    system('nose 2> /tmp/nose; sleep 1')
    return sub(r'\.\d\d\ds', r'.xxxs', shell('cat /tmp/nose'))


def process_status_test():
    '''Make sure that there are not too many processes running'''
    return limit_lines ('ps -e',190,200)


def pwd_test():
    '''List the current directory   '''
    return shell('pwd')


def system_test_list():
    '''Create a list of tests to manage'''
    return {
        'sys-nose': nose_test_execution,
        'sys-vc': vc_checker,
        'sys-cmd': cmd_checker,
        'sys-book': book_checker,
        'sys-doc': doc_checker,
        'sys-tst': tst_checker,
        'sys-pip': cmd_python_pip_test,
        'sys-ps': process_status_test,
        'sys-pwd': pwd_test,
    }


def system_checker():
    '''Execute all tests for the tst command'''
    my_tests = system_test_list()
    run_diff_checks('system', my_tests)


# Create a script that can be run from the shell
if __name__=='__main__':
    system_checker()
    