#!/usr/bin/python2
#coding=utf-8
import re
import os

pathfile = r"..\\..\\ER_\\webDate"

webfilepath = r"%s\\" %(pathfile)
#pathfile = r"..\\ER_\\webDate"
filelist = os.listdir(pathfile)
def regular():
	for key in filelist:
		print "the file name:",key
		webfile = webfilepath + key
		webfiledata = open(webfile)
		theWebMess = webfiledata.read()
		DeleteSourceData(key)
		print "The web mess:",theWebMess

def DeleteSourceData(file):
	filepath1 =  r"C:\\Users\\Administrator\\Desktop\\timp\\ER_\\webDate\\%s" % file
	filepath2 =  r"C:\\Users\\Administrator\\Desktop\\timp\\ER_\\webSourceDatas\\%s" % file
	delFile = os.remove(filepath1)
	delFile = os.remove(filepath2)
	print "the delete file :",delFile
	pass

def main():
	regular()

if __name__ == '__main__':
	main()
