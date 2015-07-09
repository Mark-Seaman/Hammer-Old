#!/usr/bin/env python
# Run all of the system tests

from datetime import datetime
from genericpath import exists
from os.path  import join, isfile, splitext, basename
from os       import system, environ, chmod, remove
from glob     import glob
from socket   import gethostname
from sys      import argv

from files import do_command, write_file, read_text
from store import save, recall, expire, expiration
from diff  import diff_string


#-----------------------------------------------------------------------------
# One Test

# Check to see if the cache is still good
def is_cached(testname):
    cache = tname(testname)+'.cache'
    if expiration(cache):
        print "Used Cached results for %s seconds"%(expiration(cache))
        return True
    else:
        return False


# Clear the cache for all tests
def clear_cache(testname):
    expire(tname(testname)+'.cache',1)


# Execute the test and save the results
def execute_test(testname):
    if not is_cached(testname) or diff(testname):
        start = datetime.now()
        if not exists(tname(testname)+'.tst'):
            print 'error: Missing command',tname(testname)+'.tst'

        text = do_command('bash '+tname(testname)+'.tst')
        end   = datetime.now()
        t     = end-start
        print "%d.%1d seconds"%(t.seconds, t.microseconds/100000)

        save(tname(testname)+'.out', text)

        save(tname(testname)+'.cache', text)
        expire(tname(testname)+'.cache', 10+t.seconds*100)


# Run the requested test as a shell script
def run(testname):
    print 'Running %-15s %-50s'%(testname, tname(testname)+'.tst'),
    execute_test(testname)
    diff(testname)


# Run all tests
def run_test(testname):
    f = join(environ['pt'],t+'.py')
    #print "\n\nTEST:",t, f, join(environ['pt'],t+'.py')
    if exists(f):
        print "py_run(",t,")",t
        run(t)
    else:
        print "sh_run(",t,")",t
        run(t)

# Return the output from the last run
def output(testname):
    return recall(tname(testname)+'.out')
    

# Lookup the correct output for the test
def correct(testname):
    correct_text = recall(tname(testname)+'.correct')
    if correct_text:
        write_file(join(environ['pt'],gethostname(),testname), [correct_text])
    return correct_text


# Correct load from Git repo
def correct_load(testname, host):
    correct_text = read_text(join(environ['pt'],host,testname))[:-1]
    save(tname(testname)+'.correct', correct_text)


# Read correct answers from Git repo files and save them
def load_correct_files(host):
    for t in tests():
        print 'Load Correct:',host,t
        correct_load(t, host)


# Accept these test results        
def like(testname):
    text = recall(tname(testname)+'.out')
    save(tname(testname)+'.correct', text)


# Decide if this is an ok result
def is_ok(testname):
    t1 = output(testname)
    t2 = correct(testname)
    if not t2:
        save(tname(testname)+'.correct',t1)
        t2 = t1
    return t1 == t2


# Calculate the difference from what was expected
def diff(testname):
    t1 = output(testname)
    t2 = correct(testname)
    if not t2:
        save(tname(testname)+'.correct',t1)
        t2 = t1
    if t1!=t2:
        print '\n_____________________________________________________\n'
        print 'FAIL:  %-35s'%testname, len(t1), len(t2)
        print '_____________________________________________________'

        print diff_string(t1,t2)
        return True
    else:
        return False


        
#-----------------------------------------------------------------------------
# Test Files

# Form the path to the test
def tname(testname):
    return join(environ['pt'],testname)

# Save this test code
def save_code(testname, code):
    save(tname(testname)+'.tst', code)


# Recall the test code
def get_code(testname):
    return write_file(tname(testname)+'.tst', recall(tname(testname)+'.tst'))


# Enumerate Tests
def tests():
    files = glob(join(environ['pt'],"*.tst"))
    files = [splitext(basename(f))[0] for f in files]
    return sorted(files)


# Show Tests Results
def tests_results():
    for t in tests():
        diff (t)


# Show Tests Results
def tests_status():
    for t in tests():
        if not is_ok (t):
            print('%s' % t)


# Clear all of the test cached results
def reset_cache():
    for t in tests():
        clear_cache(t)


# Create one tst file to execute nose on a py file
def create_test(t):
    code = 'tpyrun '+t.replace(environ['p'],'$p')+' \n'
    test = join(environ['pt'],basename(t.replace('_test',''))+'.tst')
    pc = join(environ['pt'],basename(t+'.pyc'))
    if exists(pc):
        remove (pc)
    f = open(test,'w')
    f.write(code)
    f.close()
    chmod (test, 0755)
    #print 'Create %-40s \n   %s'%(test,code)


# Translate from python tests into shell tests
def build_dir_tests(d):
    files = sorted(glob(join(d,"*_test.py")))
    files = [ join(d,f) for f in files ]
    files = filter(isfile, files)
    files = [ f.replace('.py','') for f in files ]
    for t in files:
        create_test(t)


# Run all system tests when requested
if __name__ == '__main__':
    if len(argv)>1 and argv[1]=='results':
        print('show results')
        tests_results()
    elif len(argv)>1 and argv[1]=='status':
        print('show status')
        tests_status()
    else:
        build_dir_tests(join(environ['pt']))
        build_dir_tests(join(environ['pb'],'util'))
        for t in tests():
            run(t)

