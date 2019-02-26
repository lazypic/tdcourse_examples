#coding:utf8
import redis

r = redis.Redis(host="10.10.10.172", port=6379)
r.set("kimhanwoong","0109411706")
#print r.get("baeseoyoung")
