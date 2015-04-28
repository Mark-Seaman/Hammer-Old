#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ, mkdir
from os.path import join, exists
from subprocess import Popen,PIPE
from sys import argv


def do_command(cmd):
    '''
    Run the command as a process and capture stdout & return it
    '''
    try:
        p = Popen(cmd, stdout=PIPE) #
        return  p.stdout.read()[:-1]
    except:
        return 'Command Error: %s'%cmd


def differences(answer,correct):
    '''
    Calculate the diff of two strings
    '''
    if answer!=correct:
        t1 = '/tmp/diff1'
        t2 = '/tmp/diff2'
        with open(t1,'w') as file:
            file.write(answer)
        with open(t2,'w') as file:
            file.write(correct)
        diffs = Popen([ 'diff', t1, t2 ], stdout=PIPE).stdout.read()
        print('< actual     > expected')
        print diffs
        return diffs


def tst_add(argv):
    ''' 
    Create a new tst.
    '''
    print("Add new tst:"+argv[2])
    tst = argv[2]
    path = join(environ['pb'],'%s_test.py' % tst)
    path2 = join(environ['pb'],'prototypetest.py')
    test_content = open(path2).read().replace('prototype',tst)
    #print('Content: %s_test.py \n %s' % (tst,test_content))
    with open(path,'w') as f:
        f.write(test_content)
    tst_edit(argv)


def tst_delete(argv):
    ''' 
    Delete the tst.
    '''
    print("Delete tst:",argv[2])
    system('rm  bin/%s_test.py' % argv[2])


def tst_edit(argv):
    ''' 
    Edit the content of a tst.
    '''
    print("tst:",argv[2])
    system('e bin/%s_test.py' % argv[2])


def tst_help():
    '''
    Show all the tst tsts and their usage.
    '''
    print('''
    usage: cmd tst [args]

    tst:

        add     [file] -- Add a new tst
        delete  [file] -- Delete a tst
        edit    [file] -- Edit the tst
        list    [file] -- List all tsts
        show    [file] -- Show a tst
      
            ''')


def tst_list(argv):
    '''
    List the parts of the tst source code.
    '''
    print("List the contents of this tst")
    for d in ('bin',):
        print(d+':')
        files = listdir(join(environ['p'],d))
        files = [ x for x in files if x.endswith('_test.py') ]
        print('    '+'\n    '.join(files))


def tst_show(argv):
    ''' 
    Show the content of a tst.
    '''
    print("tst:",argv[2])
    system('cat bin/%s' % argv[2])


def tst_tst(argv):
    '''
    Execute all of the tst specific tsts
    '''
    if len(argv)>1:

        if argv[1]=='add':
            tst_add(argv)
            exit(0)

        if argv[1]=='delete':
            tst_delete(argv)
            exit(0)

        if argv[1]=='edit':
            tst_edit(argv)
            exit(0)

        if argv[1]=='list':
            tst_list(argv)
            exit(0)

        if argv[1]=='show':
            tst_show(argv)
            exit(0)

        print('No tst tst found, '+argv[1])
        
    tst_help()

#------------------------------
# Specific tests to run

def pwd_test():
    return do_command('pwd')


def ls_test():
    return do_command('ls')


def source_test():
    dirs = ['','bin','test']
    result = []
    for d in dirs:
        result += glob(join(d,'*.py'))
    return '\n'.join(result)+'\n'
    

my_tests = {
    'pwd': pwd_test,
    'ls': ls_test,
    'source': source_test,
}


#------------------------------
# Test runner


def save(name, value=''):
    '''
    Save the value by its name
    '''
    #print('save',name, value)
    if not exists('test'):
        mkdir('test')
    with open('test/'+name,'w') as file:
        file.write(value)


def recall(name):
    '''
    Recall the value by its name
    '''
    if not exists('test'):
        mkdir('test')
    if exists('test/'+name):
        with open('test/'+name) as file:
            return file.read()


def run_test(name, function):
    '''
    Run the test and check the results
    '''
    answer = function()
    save('%s.out' % name, answer)
    correct = recall(name+'.correct')
    if not correct:
        save('%s.correct' % name, answer)
    differences(answer,correct)


def approve_test(name, function):
    '''
    Approve the test results
    '''
    save('%s.correct' % name, recall(name+'.out'))


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    #tst_tst(argv)

    if len(argv)>1 and 'like'==argv[1]:
        print('approve')

        for t in my_tests:
            approve_test(t, my_tests[t])

    else:
        for t in my_tests:
            run_test(t, my_tests[t])

    #print(test_results)
