from pymongo import MongoClient
import datetime

client = MongoClient("10.10.10.172", 27017)
db = client.projects
project = "circle"
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
item = {"name":"BAR_0010",
		"text":"fire and sky arwork",
		"tags":["fire","sky"],
		"date":date,
}
db["circle"].insert_one(item)
