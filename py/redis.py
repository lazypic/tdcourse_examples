#coding:utf8
import redis

r = redis.Redis(host="10.10.10.120", port=6379)
for i in range(100000):
	r.set(str(i), i)
