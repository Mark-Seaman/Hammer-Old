from os import system
from re import sub
from sys import argv

from tst import run_diff_checks, shell, lines, limit_lines


'''Execute all tests for the tst command'''
if __name__=='__main__':
    run_diff_checks('system', system_test_list())
