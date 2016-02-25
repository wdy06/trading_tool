#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import csv
import numpy as np

odata = []
for i in range(1,3):
	# HTML を取得
	url="http://info.finance.yahoo.co.jp/ranking/?kd=31&mk=3&tm=d&vl=a&p=%d" % (i)
	#print url
	html = urllib.urlopen(url).read()

	# 解析用の BeautifulSoup オブジェクトを作成
	soup = BeautifulSoup(html)

	rec=[]
	# class 属性が txtcenter である td タグを対象
	for td in soup('td',{'class':'txtcenter'}):
		for a in td('a'):
			rec.append(a.renderContents())
            	
	print rec
    odata.append(rec)

with open('ranking.csv', 'wb') as oc:
    odata = np.array(odata).transpose()
    writer = csv.writer(oc)
    writer.writerows(odata)
    print 'save ranking.csv'
