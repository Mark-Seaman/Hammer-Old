# Use Redis to set up a store for key-value pairs

from redis      import Redis


store = Redis("localhost")


# Save the item for later
def save(key,value):
    store.set(key,value)
    return key


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


def store_command(argv):
    '''Execute all of the store specific commands '''
    if len(argv)>1:

        if argv[1]=='save':
            print(save(argv[2],argv[3]))

        elif argv[1]=='recall':
            print(recall(argv[2]))

        elif argv[1]=='test':
            from store_test import store_checker
            store_checker()
