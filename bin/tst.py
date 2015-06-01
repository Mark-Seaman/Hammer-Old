#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ, mkdir
from os.path import join, exists
from subprocess import Popen,PIPE
from sys import argv

from store import save, recall, expire, expiration


def limit_lines(shell_command, min=None, max=None):
    '''Limit the lines to a certain number or echo all the output'''
    text = shell (shell_command)
    violation = lines(text,min,max)
    if violation:
        text = text.split('\n')
        text = '\n'.join([line[:60] for line in text])
        return violation+'\n'+text
    return ''


def lines(text, min=None, max=None):
    '''Guarantee that there are the correct number of lines in the text.'''
    num_lines_output = len(text.split('\n'))
    if min and num_lines_output<min:
        return('Min count lines: actual=%d, min=%d' % (num_lines_output, min))
    if max and num_lines_output>max:
        return('Max count lines: actual=%d, max=%d' % (num_lines_output, max))


def shell(command):
    '''   Execute a shell command and return its output   '''
    output = Popen(command.split(' '), stdout=PIPE).stdout
    return output.read().decode(encoding='UTF-8')


def differences(answer,correct):
    '''   Calculate the diff of two strings   '''
    if answer!=correct:
        t1 = '/tmp/diff1'
        t2 = '/tmp/diff2'
        with open(t1,'wt') as file1:
            file1.write(str(answer))
        with open(t2,'wt') as file2:
            file2.write(str(correct))
        diffs = shell('diff %s %s' %(t1, t2))
        if diffs:
            print('Differences detected:     < actual     > expected')
            print (diffs)
            return diffs


def test_list():
    '''Generate a list of test names'''
    if not exists('test'):
        mkdir('test')
    return [f.replace('.out','').replace('test/','') for f in glob('test/*.out')]


def show_output(name):
    '''Show the output text for the last test run'''
    print('Output from %s\n-----------------' % name)
    print(recall(name+'.out'))


def show_expected(name):
    '''Lookup the expected correct result for this test'''
    print('Expected correct output from %s\n-----------------' % name)
    print(recall(name+'.correct'))


def show_status():
    '''  Display the tests that failed  '''
    failures = []
    for name in test_list():
        answer = recall ('%s.out' % name)
        correct = recall('%s.correct' % name)
        if answer!=correct:
            failures.append('    %-20s FAIL' % name)
    print('\n\nTest Status: %d tests failed' % len(failures))
    print('  '+'\n    '.join(failures))
      

def show_diff(name):
    '''   Show the results for one test   '''
    answer = recall ('%s.out' % name)
    correct = recall('%s.correct' % name)
    if answer!=correct:
        print('---------------------------------------------------------')
        print('                      '+name)
        print('---------------------------------------------------------')
        print(differences(answer,correct))


def show_differences(my_tests):
    '''   Display all of the unexpected results   '''
    for name in my_tests:
        show_diff(name)


def approve_results(name):
    '''   Approve the test results   '''
    answer = recall(name+'.out')
    if answer:
        save('%s.correct' % name, answer)
    else:
        print('No output from test: '+name)
        save('%s.correct' % name, '')


def run_check(name, function):
    '''   Run the test and check the results   '''
    print('    running '+name+'...')
    answer = function()
    save('%s.out' % name, answer)
    correct = recall(name+'.correct')
    if not correct:
        save('%s.correct' % name, answer)
    show_diff(name)


def run_all_checks(label, my_tests):
    '''   Execute all of the tests defined in the dictionary.   '''
    print('Testing %s:' % label)
    for t in my_tests:
        run_check(t, my_tests[t])


def tst_help():
    '''   Show the details of the 'tst' command   '''
    print('''
    usage: tst [command] [testname]

    examples:
        tst                 # runs all the tests
        tst results         # display the differences from expected
        tst name            # runs a single test
        tst like name       # set the correct results
        tst output name     # show the output results
        tst correct name    # show the correct results
      
    subcommands of tst:

    No args
        list       # List the tests to run
        status     # Show the failing tests
        results    # Show the unexpected results

    One test arg
        output     # Show the output
        correct    # Show the correct output
        results    # Show the unexpected results

    Shortcut commands
        tlike      # tst like
        tres       # tst results
        tstatus    # tst status
        tout       # tst output
        tcorrect   # tst correct
        tst        # systest
        nose       # nosetests

    Scripts
        doc        # Documents
        cmd        # Executable commands
        vc         # Version control with git
        tst        # Testing script

            ''')


def run_diff_checks(label, my_tests):
    '''   Run the appropriate test command   '''
    run_all_checks(label, my_tests)


def tst_add(command):
    '''Create a new test.'''
    print("Add new test:"+command)
    script_path = join(environ['pb'],'%s_test.py' % command)
    template_path = join(environ['pb'],'prototypetest.py')
    command_content = open(template_path).read().replace('prototype',command)
    #print('Content: %s.py \n %s' % (command,command_content))
    if exists(script_path):
        print('File already exists: '+script_path)
    else:
        with open(script_path,'w') as f:
            f.write(command_content)
    #command_edit(argv)


def tst_edit(command):
    '''Edit the content of a test.'''
    print("Edit:",command)
    print(shell('e bin/%s_test.py' % command))


def execute_tst_command(argv):
    '''Execute the appropriate test command'''
    if len(argv)==2:
        t = argv[1]

        if 'status'==t:
            show_status()
        
        elif 'results'==t:
            print('Test differences: all tests')
            show_differences(test_list())

        elif 'list'==t:
            for t in sorted(test_list()):
                print (t)

        elif 'test'==t:
            from tst_test import tst_checker
            tst_checker()

        elif 'help'==t:
            tst_help()

        else:
            print('no test found: '+t)
            tst_help()

    elif len(argv)==3:
        cmd = argv[1]
        t = argv[2]

        if 'add'==cmd:
            tst_add(t)

        elif 'edit'==cmd:
            tst_edit(t)

        elif 'like'==cmd:
            approve_results(t)
            
        elif 'output'==cmd:
            show_output(t)

        elif 'correct'==cmd:
            show_expected(t)

        elif 'results'==cmd:
            print('Show results: %s' % t)
            show_diff(t)

        else:
            print('bad command: '+cmd)


# Create a script that can be run from the tst
if __name__=='__main__':

    if len(argv)==1:
        from systest import system_checker
        system_checker()
        show_status()

    execute_tst_command(argv)
