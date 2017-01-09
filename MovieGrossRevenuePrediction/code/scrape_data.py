import json
import requests
from bs4 import BeautifulSoup 
from six.moves import urllib
import time
import os

URLtt = 'http://www.imdb.com/title/'

startyear = 2000
endyear = 2015

yearlist = list(range(startyear,endyear+1))


for year in yearlist:

	ttnumbers = []
	title = []
	contentrating = []
	duration = []
	genres= []
	releasedate = []
	filename = '../ttnumbers/'+'tt' + str(year)+'.txt'
	inputfile = open(filename, "r")

	#1st line
	line = inputfile.readline()

	while line:
		genre = []
		line = inputfile.readline()
		line = line.strip()
		ttnumbers.append(line)
		URLmod = URLtt + line + '/?ref_=nv_sr_1'
		print URLmod
		response = urllib.request.urlopen(URLmod)
		html = response.read()
		#print html
		soup = BeautifulSoup(html,'html.parser')
		title.append(soup.title.string)
		
		
		span = soup.find_all('div', class_='subtext')
		for i in span:
			rate = i.find_all('meta')
			f = 0
			j = rate[0]
			text1 = str(j).strip()
			if text1.find('contentRating') != -1:
				f = 1
				start = text1.find('contentRating">')+15
				end = text1.find('<span',start)
				print text1[start:end].strip()
				contentrating.append(text1[start:end].strip())
			else:
				if f == 0:	
					contentrating.append('N/A')
			
			metatag = i.find_all('meta',attrs = {'itemprop':'datePublished'})
			for tag in metatag:
				text1 = str(tag)
				start = text1.find('content="')+9
				end = text1.find('"',start)
				print text1[start:end].strip()
			
			runtime = i.find_all('time')
			for j in runtime:
				runningtime = j.get_text().strip()
				duration.append(runningtime)
				print runningtime
				break
			setgenre = i.find_all('a')
			for j in setgenre:
				text = j.get('href')
				#print text
				if text.find('genre') != -1:
					print j.get_text().strip()
					genre.append(j.get_text)
				
				if text.find('releaseinfo') != -1:
					#print text
					print j.get_text().strip()
					releasedate.append(j.get_text())
					




				

		
		print soup.title.string

	genres.append(genre)
	inputfile.close()


