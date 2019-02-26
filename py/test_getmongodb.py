#coding:utf8
from pymongo import MongoClient
import datetime
p = MongoClient("10.10.10.172", 27017)
db = p.projects # dbname
project = "circle" # collection

date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

result = db[project].delete_many({"name":"김정기"})
print(result)
