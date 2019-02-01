#!/usr/bin/env python
#coding:utf8
import re

def project(path):
	"""
	경로에서 project 이름을 반환한다.
	"""
	p = re.findall('/project/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project 정보를 가지고 올 수 없습니다."
	return p[0], None

def seq(path):
	"""
	경로에서 seq 이름을 반환한다.
	"""
	p = re.findall('/shot/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 seq 정보를 가지고 올 수 없습니다."
	return p[0], None

def shot(path):
	"""
	경로에서 shot 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 shot 정보를 가지고 올 수 없습니다."
	return p[0], None

def task(path):
	"""
	경로에서 task 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/\w+/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 task 정보를 가지고 올 수 없습니다."
	return p[0], None

def ver(path):
	"""
	경로에서 version 정보를 반환한다.
	"""
	p = re.findall('_v(\d+)', path.replace("\\","/"))
	if len(p) != 1:
		return -1, "경로에서 task 정보를 가지고 올 수 없습니다."
	return int(p[0]), None

def seqnum(path):
	"""
	경로에서 시퀀스 넘버를 반환한다.
	"""
	p = re.findall('\.(\d+)\.', path.replace("\\","/"))
	if len(p) != 1:
		return -1, "경로에서 seqnum 정보를 가지고 올 수 없습니다."
	return int(p[0]), None

def digitnum(path):
	"""
	경로에서 시퀀스 넘버 자릿수를  반환한다.
	"""
	p = re.findall('\.(\d+)\.', path.replace("\\","/"))
	if len(p) != 1:
		return -1, "경로에서 seqnum 정보를 가지고 올 수 없습니다."
	return len(p[0]), None

def toFFmpeg(path):
	"""
	경로를 받아서 시퀀스라면 ffmpeg 경로로 바꾸어준다.
	"""
	p = re.findall('\.(\d+)\.', path.replace("\\","/"))
	if len(p) != 1:
		return path, "경로가 시퀀스 구조가 아닙니다."
	digitNum = len(p[0])
	head, tail = path.split(p[0])
	return "%s%%%dd%s" % (head,digitNum,tail), None
