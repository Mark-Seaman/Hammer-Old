# Build a dictionary for a list of unique items grouped into categories.

index = dict()

# If key is found then add the item to the set.  Otherwise create a set.
def add_item(key, item):
    global index
    index.setdefault(key, set()).add(item)

# Run test cases
def test_it():
    add_item('x',3)
    add_item('x',14)
    add_item('x',5)
    add_item('x',14)
    add_item('y',5)
    add_item('y',1)
    print index

# When run stand alone then do the test
if __name__ == '__main__':
    test_it()
