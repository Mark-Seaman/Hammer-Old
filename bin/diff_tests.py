#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ, mkdir
from os.path import join, exists
from subprocess import Popen,PIPE
from sys import argv


def lines(text, min=None, max=None):
    '''
    Guarantee that there are the correct number of lines in the text.
    '''
    num_lines_output = len(text.split('\n'))
    if min and num_lines_output<min:
        return('Min count lines: actual=%d, min=%d' % (num_lines_output, min))
    if max and num_lines_output>max:
        return('Max count lines: actual=%d, max=%d' % (num_lines_output, max))


def shell(command):
    '''
    Execute a shell command and return its output
    '''
    return str(Popen(command.split(' '), stdout=PIPE).stdout.read())


def differences(answer,correct):
    '''
    Calculate the diff of two strings
    '''
    if answer!=correct:
        t1 = '/tmp/diff1'
        t2 = '/tmp/diff2'
        with open(t1,'wt') as file:
            file.write(answer)
        with open(t2,'wt') as file:
            file.write(correct)
        diffs = str(Popen([ 'diff', t1, t2 ], stdout=PIPE).stdout.read())
        print('< actual     > expected')
        print (diffs)
        return diffs


def save(name, value=''):
    '''
    Save the value by its name
    '''
    #print('save',name, value)
    if not exists('test'):
        mkdir('test')
    with open('test/'+name,'wt') as file:
        file.write(value)


def recall(name):
    '''
    Recall the value by its name
    '''
    if not exists('test'):
        mkdir('test')
    if exists('test/'+name):
        with open('test/'+name) as file:
            return str(file.read())


def show_output(name):
    print(recall(name+'.out'))


def show_expected(name):
    print(recall(name+'.correct'))


def run_check(name, function):
    '''
    Run the test and check the results
    '''
    answer = function()
    save('%s.out' % name, answer)
    correct = recall(name+'.correct')
    if not correct:
        save('%s.correct' % name, answer)
    differences(answer,correct)


def approve_results(name, function):
    '''
    Approve the test results
    '''
    save('%s.correct' % name, recall(name+'.out'))


def run_all_checks(my_tests):
    '''
    Execute all of the tests defined in the dictionary.
    '''
    for t in my_tests:
        print('running '+t+'...')
        run_check(t, my_tests[t])


def tst_help():
    '''
    Show the details of the 'tst' command
    '''
    print('''
    usage: tst [command] [testname]

    examples:
        tst                 # runs all the tests
        tst name            # runs a single test
        tst approve name    # set the correct results
        tst answer name     # show the output results
        tst expected name   # show the correct results
      
            ''')


def system_test():
    '''
    Check the checker
    '''
    def dummy_test():
         return 'pass'
    run_all_checks({'dummy': dummy_test})


def execute_command(argv, my_tests):
    '''
    Run the appropriate test command
    '''
    if len(argv)>2:
        t = argv[2]
        if 'approve'==argv[1]:
            print('approve results '+t)
            if t in my_tests:
                approve_results(t, my_tests[t])
            else:
                print('no test found: '+t)
                tst_help()
        if 'answer'==argv[1]:
            print('output from %s\n-----------------' % t)
            show_output(t)
        if 'expected'==argv[1]:
            print('expected from %s\n-----------------' % t)
            show_expected(t)
    else:
        if len(argv)>1:
            t = argv[1]
            print(my_tests)
            if t in my_tests:
                run_check(t, my_tests[t])
            else:
                print('no test found: '+t)
                tst_help()
        else:
            run_all_checks(my_tests)
