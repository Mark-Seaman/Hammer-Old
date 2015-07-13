def redis_test():
    import redis
    s = redis.Redis("localhost")
    assert(s.set('name','Mark'))
    assert(s.get('name')=='Mark')
    assert(s.set('name','Bill'))
    assert(s.get('name')=='Bill')

print 'Testing Redis'
redis_test()
