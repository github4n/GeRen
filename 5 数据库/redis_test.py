from redis import StrictRedis,ConnectionPool

# redis = StrictRedis(host='localhost',port=6379)
# redis.set('name','Bob')
# print(redis.get('a'))

url = 'redis://:@localhost:6379'

pool = ConnectionPool.from_url(url)

redis = StrictRedis(connection_pool=pool)

# 字符串
redis.set('name','Bob')
print(redis.get('name'))
print(redis.type('a'))
print(redis.get(redis.randomkey()))
print(redis.getset('name','Mike'))
print(redis.get('name'))

#列表
print(redis.rpush('list',1,2,3,4,5,6,7,8,9))
print(redis.lindex('list',3))

#集合
print(redis.sadd('set',1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9))
print(redis.scard('set'))

#有序集合
print(redis.zadd('grade',100,'Bob','88','Mike'))
print(redis.zrank('grade','Bob'))

#Hash
print(redis.hmset('hash',{'bans':2,'apple':4}))
print(redis.hgetall('hash'))

#删除所有数据库的所有键
# print(redis.flushall())
















