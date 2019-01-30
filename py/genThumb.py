#!/usr/bin/env python
#coding:utf8
import os
import sys
import subprocess

def genThumb(src):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	if not os.path.exists("/usr/bin/convert"):
		return "", "ImageMagick이 설치되지 않았습니다."

	d, f = os.path.split(src)
	notuse, ext = os.path.splitext(f)
	dst = d+"/"+f.replace(ext,".jpg")
	size="360x240"
	cmds = ["convert", src, "-thumbnail", size,
			"-background", "black", "-gravity", "center",
			"-extent", size, dst]
	p = subprocess.Popen(cmds,
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE)
	return p.communicate()

if __name__ == "__main__":
	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078727.exr"
	stdOut, stdErr = genThumb(src)
	if stdErr:
		sys.stderr.write(stdErr)
	sys.stdout.write(stdOut)

