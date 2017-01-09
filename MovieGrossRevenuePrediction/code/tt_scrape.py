import json
import requests
from bs4 import BeautifulSoup 
from six.moves import urllib
import time
import os
URLstart = 'http://www.imdb.com/search/title?sort=boxoffice_gross_us,desc&start='
usertitles = 200



pages = int(usertitles / 50)
startyear = 2000
endyear = 2015

yearlist = list(range(startyear,endyear+1))



for year in yearlist:
	ttlist = []
	URLyear = '&year=' + str(year) + ',' + str(year)

	for page in range(pages):
		URLshell = URLstart + str((page*50)+1) + URLyear
		response = urllib.request.urlopen(URLshell)
		print URLshell
		html = response.read()
		#print html
		soup = BeautifulSoup(html,'html.parser')
		

		print soup.title.string


		span = str(soup.find_all('span',{'class':"userRatingValue"}))
		spanlist = span.split(',')
		#print spanlist
		for item in spanlist:
			start = item.find('data-tconst="')+13
			end = item.find('"',start)
			tt = item[start:end]
			ttlist.append(tt)

	filename = '../ttnumbers/'+'tt'+str(year)+'.txt'
	dir = os.path.dirname(filename)
	if not os.path.exists(dir):
		os.makedirs(dir)
	with open(filename, 'w')  as outputfile:
		for i in ttlist:
			outputfile. write(i) 
			outputfile. write(' \n')




