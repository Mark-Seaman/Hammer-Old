'''
Tests for shell code
-------------------

Run all of the tests for the 'shell' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join


def shell_add_delete_test():
    from shell import shell
    results = [
        shell('shell list xxx'),
        shell('shell show xxx'),
        shell('shell add_test xxx'),
        shell('shell list xxx'),
        shell('shell show xxx'),
        shell('shell delete xxx'),
        shell('shell list xxx'),
    ]
    return '\n'.join(results)


def shell_list_test():
    from shell import shell
    return shell('shell list')


def shell_path_test():
    from shell import shell
    return shell('shell path') + '\n' + shell('shell path xxx')


def shell_show_test():
    from shell import shell
    return shell('shell show')
