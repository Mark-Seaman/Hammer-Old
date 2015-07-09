# Calculate the difference between two dictionaries as:
#    items added
#    items removed
#    keys same in both but changed values
#    keys same in both and unchanged values

from collections import OrderedDict


# Compare two dictionaries to identify all changes
class DictDiffer(object):

    def __init__(self, current, past):
        self.current, self.past = current, past
        self.set_current, self.set_past = set(current.keys()), set(past.keys())
        self.intersect = self.set_current.intersection(self.set_past)

    def added(self):
        return self.set_current - self.intersect 

    def removed(self):
        return self.set_past - self.intersect 

    def changed(self):
        return set(o for o in self.intersect if self.past[o] != self.current[o])

    def unchanged(self):
        return set(o for o in self.intersect if self.past[o] == self.current[o])

    def diff(self):
        results = []
        for x in self.added():
            results.append('< '+x+' '+self.current[x])
            results.append('')
        for x in self.removed():
            results.append('> '+x+' '+self.past[x])
            results.append('')
        for x in self.changed():
            results.append('< '+x+' '+self.current[x])
            results.append('> '+x+' '+self.past[x])
            results.append('')
        return '\n'.join(results)
          

# Convert a block of text to a dictionary
def to_dict(text):
    p = OrderedDict()
    for x in text.split('\n'):
        x = x.split(' ')
        if len(x)==2:
            p[x[1]] = x[0]
    return p


# Return the difference in two text blocks of counters  
def dict_diff(current,past):
    return DictDiffer(to_dict(current),to_dict(past)).diff()
