# Calculate the difference between two dictionaries as:
#    items added
#    items removed
#    keys same in both but changed values
#    keys same in both and unchanged values

from dictdiff import DictDiffer


def test_dict():

    a = {'a': 1, 'b': 1, 'c': 0}
    b = {'a': 1, 'b': 2, 'd': 0}
    d = DictDiffer(b, a)

    print "Added:", d.added()
    print "Removed:", d.removed()
    print "Changed:", d.changed()
    print "Unchanged:", d.unchanged()


