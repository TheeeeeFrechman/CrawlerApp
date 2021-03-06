#!/usr/bin/python2
#coding=utf-8
import re
import os
import sys
import time
import urllib2
import lxml.html
from bs4 import BeautifulSoup
#sys.path.append("..\\..\\regular\\source\\")
#sfrom regular import regular
_Time = time.time()
filename = "ERBeautifulSouphtml%s.html" %(_Time)
htmlfile = "ERHtml%s.html" %(_Time)
Htmlfile = r"..\\webDate\\%s" %(filename)
htmlfile = r"..\\webSourceDatas\\%s" %(htmlfile)
def download(url, user_agent='wswp', num_reries = 2):
	print 'Downloading',url
	headers = {'User-agent':user_agent}
	request = urllib2.Request(url, headers=headers)
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Downloading error:',e.reason
		html = None
		if num_reries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download(url,num_retries-1)
	return html

def BetSoup(html):
	soup = BeautifulSoup(html)
	webData = soup.prettify()
	writeFiledata(html,webData)
	return webData

def LxmlHtml(htmlbuff):
	broken_html = htmlbuff
	tree = lxml.html.fromstring(broken_html)
	fixed_html = lxml.html.tostring(tree, pretty_print=True)
	return fixed_html

def crawl_sitemap(url):
	sitemap = download(url)
	#print "the sitemap is:"
	#print sitemap
	#BetSoup(sitemap)
	sitemap = LxmlHtml(sitemap)
	print sitemap
	links = re.findall(r"<a.*?href=.*?<\/a>",sitemap)
	for link in links:
		print "Url:",link
		html = download(link)
		#BetSoup(html)

def writeFiledata(html,webData):
	betf = open(Htmlfile,"w+")
	htmldata = open(htmlfile,"w+")
	wirteDatanum = betf.write(webData.encode("utf-8"))
	if wirteDatanum == "" or wirteDatanum == None :
		print "----beautiful soup file is faile----"
	else:
		print "the data num:",wirteDatanum
	wirteDatehtml = htmldata.write(html)
	if wirteDatehtml == "" or wirteDatehtml == None:
		print "----file is faile----"
	else:
		print "the htmldata num:",wirteDatanum
	

def main():
	crawl_sitemap("http://www.huaban.com")

if __name__ == "__main__":
		main()