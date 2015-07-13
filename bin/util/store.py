# Use Redis to set up a store for key-value pairs

from redis      import Redis

store = Redis("localhost")


# Save the item for later
def save(key,value):
    store.set(key,value)


# Recall a previously stored item
def recall(key):
    return store.get(key)


# Set the expiration time in seconds
def expire(key,seconds):
    store.expire(key,seconds)


#  Check the expiration time
def expiration(key):
    return store.ttl(key)

