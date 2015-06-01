# Use Redis to set up a store for key-value pairs

from redis      import Redis
from sys import argv


store = Redis("localhost")


# Save the item for later
def save(key,value):
    store.set(key,value)


# Recall a previously stored item
def recall(key):
    value = store.get(key)
    if value:
        return value.decode(encoding='UTF-8')


# Set the expiration time in seconds
def expire(key,seconds):
    store.expire(key,seconds)


#  Check the expiration time
def expiration(key):
    return store.ttl(key)


# Create a script that can be run from the tst
if __name__=='__main__':

    if len(argv)>1 and argv[1]=='test':
        print('self test for redis')
        save('test/save', 'this is a saved key from store.py')
        print('recall:'+recall('test/save'))
    else:
        print('bad arguments:  '+' '.join(argv))

