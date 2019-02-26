#!/usr/bin/env python
#coding:utf8
import os
import csv


csvPath = os.path.expanduser("~/examples/csv/cglist.csv")
with open(csvPath) as p:
	csvReader = csv.reader(p, delimiter=',')
	for row in list(csvReader)[1:]:
		print(row)
