#!/usr/bin/env python
#coding:utf8

import os
from edl import Parser

edlfile = os.path.expanduser("~/examples/edl/lazypic_example.edl")
parser = Parser("23.98")
with open(edlfile) as p:
	edl = parser.parse(p)
	for event in edl.events:
		print "Event Number:" + str(event.num)
		print "Source file:" + str(event.source_file)
		print "Clip Name:" + str(event.clip_name)
		print dir(event)
