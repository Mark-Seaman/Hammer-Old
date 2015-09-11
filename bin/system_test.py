'''
Tests for system code
-------------------

Run all of the tests for the 'system' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join
from glob import glob

from shell import shell, lines, limit_lines


def system_python_pip_test():
    '''Check the python setup for pip'''
    return shell('pip list')


def system_nose_test_execution():
    '''Run all nose tests  and report any changes'''
    system('nose 2> /tmp/nose; sleep 1')
    return sub(r'\d\.\d\d\ds', r'x.xxxs', shell('cat /tmp/nose'))


def system_process_status_test():
    '''Make sure that there are not too many processes running'''
    return limit_lines ('ps -e',150,260)


def system_pwd_test():
    '''List the current directory   '''
    return shell('pwd')


def system_add_test():
    f = join(environ['b'],'xxx')
    open(f,'w').write('xxx')
    return shell('system add xxx') + shell('system delete xxx')


def system_delete_test():
    return shell('system delete xxx')


def system_edit_test():
    return shell('system edit xxx')


def system_list_test():
    return shell('system list xxx')


def system_show_test():
    return shell('system show project-env')


def system_shell_test():
    dir = [ 'Test directory: ' + environ['pt'] ]
    return '\n'.join (dir + glob(join(environ['pt'], '*.tst')))
