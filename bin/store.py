# Use Redis to set up a store for key-value pairs

from os import getcwd
from os.path import join
from redis      import Redis


store = Redis("localhost")


def save(key,value):
    '''Save the item for later'''
    store.set(key,value)
    return key


def recall(key):
    '''Recall a previously stored item'''
    value = store.get(key)
    if value:
        return value.decode(encoding='UTF-8')


def expire(key,seconds):
    '''Set the expiration time in seconds'''
    store.expire(key,seconds)


def expiration(key):
    ''' Check the expiration time'''
    return store.ttl(key)


def set_cache(key, value, duration):
    cache = cache_key(key)
    save(cache,value)
    if duration:
        expire(cache, duration)
        #print ("Key: %s, Duration: %s" % (cache,expiration(cache)))


def save_key(key,value,duration=None):
    '''Save the value with a key prefixed to the current directory'''
    key = join(getcwd(), key)
    #print('save_key: %s, %s, %s, %s' % (key,cache_key(key),str(value),str(duration)))
    if not value:
        value='No test script output'
    save(key, value)
    set_cache(key, value, duration)


def recall_key(key):
    '''recall_key the value with a key prefixed to the current directory'''
    return recall(join(getcwd(), key))


def cache_key(key):
    '''Name of the cache key'''
    return join(getcwd(), key+'.cache')


def is_cached(key):
    '''Check the cache to see if result is available'''
    cache = cache_key(key)
    if expiration(cache):
        #print("Used Cached results for %s seconds"%(expiration(cache)))
        return expiration(cache)
    

def clear_cache(key):
    '''Clear the cache for all tests'''
    cache = join(getcwd(), key+'.cache')
    expire(cache,1)


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
