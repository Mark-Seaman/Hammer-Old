#!/usr/bin/env python

from datetime import datetime
from glob import glob
from os import system, listdir, environ, mkdir, getcwd, chdir
from os.path import join, exists
from subprocess import Popen,PIPE
from sys import argv

from store import save, recall, expire, expiration, save_key, recall_key
from store import is_cached, clear_cache


def approve_all_answers():
    '''Automatically accept any answer'''
    for name in test_list():
        approve_results(name)


def approve_results(name):
    '''   Approve the test results   '''
    answer = recall_key(name+'.out')
    if answer:
        save_key('%s.correct' % name, answer)
    else:
        print('No test script output: '+name)
        save_key('%s.correct' % name, 'No test script output')


def reset_test_names():
    '''Reset the list of available tests'''
    open('.test','w').close()


def record_test_names(tests):
    '''Add this test to the list of available tests'''
    with open('.test','a') as openfile:
        openfile.write('\n'.join(tests)+'\n')


def test_list():
    '''Generate a list of test names'''
    return [t for t in open('.test').read().split('\n') if t]


def show_output(name):
    '''Show the output text for the last test run'''
    print('Output from %s\n-----------------' % name)
    print(recall_key(name+'.out'))


def show_expected(name):
    '''Lookup the expected correct result for this test'''
    print('Expected correct output from %s\n-----------------' % name)
    print(recall_key(name+'.correct'))

def show_status():
    '''Display the tests that failed'''
    failures = []
    for name in test_list():
        answer = recall_key ('%s.out' % name)
        correct = recall_key('%s.correct' % name)
        if answer!=correct:
            failures.append('    %-20s FAIL' % name)
    print('\n\nTest Status: %d tests failed' % len(failures))
    print('  '+'\n  '.join(failures))
      

def diff(name):
    '''Find the differences'''
    from shell import differences
    answer = recall_key ('%s.out' % name)
    correct = recall_key('%s.correct' % name)
    if answer!=correct:
        return differences(answer,correct)


def show_diff(name):
    '''Show the results for one test'''
    answer = recall_key ('%s.out' % name)
    correct = recall_key('%s.correct' % name)
    d = diff(name)
    if d:
        print('---------------------------------------------------------')
        print('                      '+name)
        print('---------------------------------------------------------')
        print(d)


def show_differences(my_tests):
    '''   Display all of the unexpected results   '''
    for name in my_tests:
        show_diff(name)


# def run_check(name, function):
#     '''   Run the test and check the results   '''
#     cache = is_cached('%s.out' % name )
#     if cache and not diff(name):
#         print("    cached results %-20s  ... %d seconds" % (name,cache))
#         answer = recall_key(name+'.out')
#     else:
#         answer = execute_test(name, function)
#     correct = recall_key(name+'.correct')
#     if not correct:
#         save_key('%s.correct' % name, answer)
#     show_diff(name)


# def run_all_checks(label, my_tests):
#     '''   Execute all of the tests defined in the dictionary.   '''
#     print('Testing %s:' % label)
#     for t in my_tests:
#        run_check(t, my_tests[t])
#     record_test_names(my_tests.keys())


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
        accept     # Accept every answer
        list       # List the tests to run
        status     # Show the failing tests
        results    # Show the unexpected results
        functions  # List the test functions for all modules
        cases      # List all test cases
        modules    # List all test modules

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

            ''')


def run_diff_checks(label, my_tests):
#     '''   Run the appropriate test command   '''
#     run_all_checks(label, my_tests)
    print("run_diff_checks is obsolete")


def tst_add(command):
    '''Create a new test.'''
    print("Add new test:"+command)
    script_path = join(environ['pb'],'%s_test.py' % command)
    template_path = join(environ['pb'],'prototype_test.py')
    command_content = open(template_path).read().replace('prototype',command)
    if exists(script_path):
        print('File already exists: '+script_path)
    else:
        with open(script_path,'w') as f:
            f.write(command_content)


def tst_edit(command):
    '''Edit the content of a test.'''
    from shell import shell
    print(shell('e bin/%s_test.py' % command))


def execute_tst_command(argv):
    '''Execute the appropriate test command'''
    if len(argv)==2:
        t = argv[1]

        if 'accept'==t:
            approve_all_answers()

        elif 'cases'==t:
            tst_cases()

        elif 'functions'==t:
            tst_functions()

        elif 'status'==t:
            show_status()
        
        elif 'results'==t:
            print('Test differences: all tests')
            #show_differences(test_list())
            tst_results()

        elif 'names'==t:
            print('\n'.join(tst_modules()))

        elif 'list'==t:
            for t in sorted(test_list()):
                print (t)

        elif 'modules'==t:
            print('\n'.join(tst_modules()))

        elif 'test'==t:
            tst_execute_all()

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

        elif 'execute'==cmd:
            tst_execute_module(t+'_test.py')

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

def tst_execute_all():
    '''Execute all of the test functions for module'''
    print('execute all')
    from code import find_functions
    for m in tst_modules():
        tst_execute_module(m)


def tst_execute_module(module):
    '''Execute all of the test functions for module'''
    print('\n'+module)
    from code import find_functions
    path = join(environ['pb'],module)
    for f in find_functions(path):
        if f.endswith('_test'):
            tst_execute_test_case(module,f)


def test_case_name(function):
    '''Convert function name to test case name'''
    return function.replace('_test','').replace('_','-')


def tst_execute_test_case(module, function):
    '''Run the selected test and process results'''
    import_name = module.replace('.py','')
    testcase = test_case_name(function)
    tst_run_case(testcase, import_name, function)


def tst_execute_timed_test(testcase, import_name, function):
    '''Execute the test and cache the results for an appropriate time'''
    start = datetime.now()
    exec("import "+import_name)
    exec("answer = %s.%s()" % (import_name,function))
    end   = datetime.now()

    t     = end-start
    seconds = "%d.%1d seconds"%(t.seconds, t.microseconds/100000)
    duration = 10+t.seconds*100
    print('    %-20s  ... %s '%(testcase,seconds))
    
    save_key('%s.out' % testcase, answer, duration)
    return answer


def tst_run_case(testcase, import_name, function):
    '''   Run the test and check the results   '''
    cache = is_cached('%s.out' % testcase )
    if cache and not diff(testcase):
        print("    cached results %-20s  ... %d seconds" % (testcase,cache))
        answer = recall_key(testcase+'.out')
    else:
        tst_execute_timed_test(testcase, import_name, function)
    correct = recall_key(testcase+'.correct')
    if not correct:
        save_key('%s.correct' % testcase, answer)
    show_diff(testcase)


def tst_modules():
    '''Enumerate all of the test command modules'''
    modules = [c for c in listdir(environ['pb']) if c.endswith('_test.py')]
    return sorted(modules)


def tst_functions():
    '''Enumerate all of the test command functions'''
    from code import find_functions
    for m in tst_modules():
        path = join(environ['pb'],m)
        for f in find_functions(path):
            if f.endswith('_test'):
                print(f)

   
def tst_cases():
    '''Enumerate all of the test command functions'''
    from code import find_functions
    for m in tst_modules():
        print('\n'+m)
        path = join(environ['pb'],m)
        for f in find_functions(path):
            if f.endswith('_test'):
                print('    '+test_case_name(f))


def tst_results():
    from code import find_functions
    cases = []
    for m in tst_modules():
        path = join(environ['pb'],m)
        for f in find_functions(path):
            if f.endswith('_test'):
                cases.append(test_case_name(f))
    for t in cases:
        show_diff(t)


# Create a script that can be run from the tst
if __name__=='__main__':

    from shell import shell
    chdir(environ['p'])
    if len(argv)==1:
        tst_execute_all()
    else:
        execute_tst_command(argv)
