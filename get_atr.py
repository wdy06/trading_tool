# -*- coding:utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import sys
import math

str=raw_input('銘柄コードを入力してください:')
number=int(str)
print number

url="http://stocks.finance.yahoo.co.jp/stocks/history/?code=%d.T"%(number)
html = urllib.urlopen(url).read()
print url

soup = BeautifulSoup(html,"html.parser")

open=[]
high=[]
low=[]
close=[]


divs=soup.find('div',{'class':'padT12 marB10 clearFix'})
day=0
count=0
for trs in divs.find_all("tr"):
	for tds in trs.find_all("td"):
		x=tds.renderContents()
		
		x=x.replace(",", "")
		if day!=0:
			if count==1:
				open.append(float(x))
				
			elif count==2:
				high.append(float(x))
				
			elif count==3:
				low.append(float(x))
				
			elif count==4:
				close.append(float(x))
				
			count=count+1
			if count==7:
				count=0
	day=day+1
			
print(open)
print(high)
print(low)
print(close)

sum=0
for i in range(1,14):
	atr=[]
	atr.append(math.fabs(high[i]-low[i]))
	atr.append(math.fabs(high[i]-close[i-1]))
	atr.append(math.fabs(low[i]-close[i-1]))
	sum=sum+max(atr)
print u"atr is %f"% (sum/14)
print u"2atr is %f" % (2*(sum/14))

	
