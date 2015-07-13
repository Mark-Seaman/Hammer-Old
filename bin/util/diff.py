from subprocess import Popen,PIPE

from files import write_file


# Calculate the diff of two strings
def diff_string (s1, s2):
    t1 = '/tmp/diff1'
    t2 = '/tmp/diff2'
    write_file (t1, s1.split('\n'))
    write_file (t2, s2.split('\n'))
    diffs = Popen([ 'diff', t1, t2 ], stdout=PIPE).stdout.read()
    return diffs


# Test the function
def test_diff():
    x = '45\nsd\ndf\nasdf\n77'
    y = '45\nsd\nfsdf\ndsadf\n77\nfasdsdf'

    print diff_string (x,y)

#test_diff()
