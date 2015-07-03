'''
Tests for system code
-------------------

Run all of the tests for the 'system' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def cmd_python_pip_test():
    '''Check the python setup for pip'''
    return shell('pip list')


def nose_test_execution():
    '''Run all nose tests  and report any changes'''
    system('nose 2> /tmp/nose; sleep 1')
    return sub(r'\d\.\d\d\ds', r'x.xxxs', shell('cat /tmp/nose'))


def process_status_test():
    '''Make sure that there are not too many processes running'''
    return limit_lines ('ps -e',150,260)


def pwd_test():
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
    print('Test directory: ' + environ['pt'])


def system_checker():
    my_tests = {
        #'nose': nose_test_execution,
        'system-pip': cmd_python_pip_test,
        'system-ps': process_status_test,
        'system-pwd': pwd_test,
        'system-add': system_add_test,
        'system-list': system_list_test,
        'system-delete': system_delete_test,
        'system-show': system_show_test,
        'system-shell': system_shell_test,
    }
    run_diff_checks('system', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    system_checker()
