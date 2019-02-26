#!/usr/bin/env python
#coding:utf8
import json

with open("data.json") as f:
	data = json.load(f)

print(data)
