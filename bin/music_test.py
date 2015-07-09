'''
Tests for music code
-------------------

Run all of the tests for the 'music' objects.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

from tst import run_diff_checks, shell, lines, limit_lines


def music_add_test():
    return shell('echo music add xxx')


def music_delete_test():
    return shell('echo music delete xxx')


def music_edit_test():
    return shell('echo music edit xxx')


def music_list_test():
    return shell('echo music list xxx')


def music_show_test():
    return shell('echo music show xxx')


def music_checker():
    my_tests = {
        'music-add': music_add_test,
        'music-list': music_list_test,
        'music-delete': music_delete_test,
        'music-show': music_show_test,
    }
    run_diff_checks('music', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    music_checker()
