#!/usr/bin/env python
#coding:utf8
import unittest
from pathapi import *

class Test_path(unittest.TestCase):
	def test_project(self):
		self.assertEqual(project("/project/circle"), ("circle", None))
		self.assertEqual(project("/project/circle/"), ("circle", None))
		self.assertEqual(project("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("circle", None))
		self.assertEqual(project("\\\\10.20.30.40\\project\\circle\\"), ("circle", None))
		self.assertEqual(project("\\\\10.20.30.41\\server1\\project\\circle\\"), ("circle", None))
		self.assertEqual(project("/server1/project/circle"), ("circle", None))
		self.assertEqual(project("/server2/project/circle"), ("circle", None))

	def test_seq(self):
		self.assertEqual(seq("/project/circle/shot/FOO"), ("FOO", None))
		self.assertEqual(seq("/project/circle/shot/FOO/"), ("FOO", None))
		self.assertEqual(seq("/project/circle/shot/S001/"), ("S001", None))
		self.assertEqual(seq("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("FOO", None))

	def test_shot(self):
		self.assertEqual(shot("/project/circle/shot/FOO/0010"), ("0010", None))
		self.assertEqual(shot("/project/circle/shot/FOO/0010/"), ("0010", None))
		self.assertEqual(shot("/project/circle/shot/S001/C0010/"), ("C0010", None))
		self.assertEqual(shot("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("0010", None))

	def test_task(self):
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp"), ("comp", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp/"), ("comp", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/model/"), ("model", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"), ("comp", None))

	def test_ver(self):
		self.assertEqual(ver("FOO_0010_comp_v001.nk"), (1, None))
		self.assertEqual(ver("FOO_0010_comp_v0003.nk"), (3, None))
		self.assertEqual(ver("FOO_0010_comp_v010.nk"), (10, None))
		self.assertEqual(ver("FOO_0010_comp_v2.nk"), (2, None))
		self.assertEqual(ver("FOO_0010_comp_v30.nk"), (30, None))

	def test_seqnum(self):
		self.assertEqual(seqnum("FOO_0010_comp_v001.1001.exr"), (1001, None))
		self.assertEqual(seqnum("FOO_0010_comp_v010.1100.exr"), (1100, None))
		self.assertEqual(seqnum("FOO_0010_comp_v010.12345.exr"), (12345, None))
		self.assertEqual(seqnum("FOO_0010_comp_v010.123456.exr"), (123456, None))
		self.assertEqual(seqnum("FOO_0010_comp_123456.exr"), (123456, None))

if __name__ == "__main__":
	unittest.main()
