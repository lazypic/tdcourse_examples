#coding:utf8
#1. 폴더를 탐색한다. "/project/circle/in/aces_exr"
#1.1 proxy 경로를 생성한다.
#2. exr로 jpg를 만든다.
#3. jpg로 mov를 만든다.
#4. jpg를 삭제한다.
import os
import sys
import subprocess
import pathapi

def searchExt(rootPath, ext):
	"""
	rootPath 경로에서 ext 확장자를 가진 파일경로를 list로 반환한다.
	"""
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if root == rootPath:
			continue
		for f in files:
			basename, e = os.path.splitext(f)
			if e != ext:
				continue
			results.append("/".join([root]+dirs+[f]))
	return results

def genProxy(proxy, files):
	"""
	file 리스트를 받아서 proxy경로에 
	프록시 이미지를 생성한다.
	"""
	for src in files:
		p, f = os.path.split(src)
		basename, ext = os.path.splitext(f)
		proxyDir = proxy + p
		if not os.path.exists(proxyDir):
			os.makedirs(proxyDir)
		dst = proxyDir + "/" + basename + ".jpg"
		cmds = ["convert", src, dst]
		p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		if err:
			sys.stderr.write(err)
		sys.stdout.write(out)

def genMov(rootPath, ext):
	"""
	path 경로에 있는 파일을 이용해서 mov를 생성한다.
	"""
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if not files:
			continue
		files.sort()
		start = "/".join([root] + dirs + [files[0]])
		end =  "/".join([root] + dirs + [files[-1]])
		seqfile, err = pathapi.path2ffmpeg(start)
		if err:
			sys.stderr.write(err)
		startframe, err = pathapi.seqnum(start)
		if err:
			sys.stderr.write(err)
		endframe, err = pathapi.seqnum(end)
		if err:
			sys.stderr.write(err)
		print seqfile, startframe, endframe

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	proxy = "/tmp/proxy"
	items = searchExt(root,".exr")
	#genProxy(proxy, items)
	genMov(proxy + root, ".jpg")


