#!/usr/bin/env python
# Work flow manager


from os  import system
from sys import argv
from store import save,recall

# Build a dictionary for a list of unique items grouped into categories.
index = {}


# If key is found then add the item to the set.  Otherwise create a set.
def add_item(key, item):
    global index
    index.setdefault(key, set()).add(item)

# If key is found then add the item to the set.  Otherwise create a set.
def delete_item(key, item):
    global index
    index.setdefault(key, set()).remove(item)


# Get the key if available
def lookup (key, value=None):
    if index.has_key(key):
        if value:
            for i in index[key]:
                if value in i:
                    print 'xxxxxxxxxx', i
            return '\n   '.join(index[key])
        else:
            return '\n   '.join(index[key])
    else:
        print 'No Match', key


# Forget everything
def clear_index():
    save('workflow', {})


# Do the lookup and format the result as text
def print_lookup(key):
    print '\nLookup:',key,'\n  ',lookup(key)


# Do the add and format the result
def print_add(key,value):
    add_item(key,value)
    print  '\nAdd:', key, '(', value, ')'


# Do the add and format the result
def print_delete(key,value):
    delete_item(key,value)
    print  '\nDelete:', key, '(',  value, ')'


# Dump the data dictionary
def print_index():
    print 'Index:'
    for i in index:
        print i
        for s in index[i]:
            print '   ', s


# Add, remove and list entries
def workflow(cmd):

    if cmd == 'print':
        print_index()
        return

    if cmd == 'run self test':
        test_workflow()
        return

    parms = cmd.split(' ')
    value = ' '.join(parms[2:])

    # Record a new entry
    if len(parms)>2 and parms[1]=='+':
        print_add(parms[0],value)
        return

    # Delete an existing entry
    if len(parms)>2 and parms[1]=='-':
        print_delete(parms[0], value)
        return

    # Find objects that match
    if len(parms)<2:

        # List all objects
        if len(parms)==0:
            print 'List: All available objects\n'
            return

        # List one object type
        if len(parms)==1:
            print_lookup(parms[0])
            return

    value = ' '.join(parms[1:])
    print 'LOOKUP:',parms[0], value
    print_lookup(parms[0])



# Run test cases
def test_index():
    add_item('x',3)
    add_item('x',14)
    add_item('x',5)
    add_item('x',14)
    add_item('y',5)
    add_item('y',1)
    print index


def test_workflow():
    test_cases = '''workflow
done + New work accomplishment
done
done - New work accomplishment
done
task + New task 1
task + New task 2
task + New task 3
task - New task 2
task
task New task 3
done + New work accomplishment
done accomplishment
task + Another task
task - Another task
task task
task 3
print
'''.split('\n')
    for f in test_cases:
        workflow (f)

   
# When run stand alone then do the test
if __name__ == "__main__":
    clear_index()
    index = eval(recall('workflow'))
    cmd = ' '.join(argv[1:])
    workflow(cmd)
    save('workflow', index)


  
