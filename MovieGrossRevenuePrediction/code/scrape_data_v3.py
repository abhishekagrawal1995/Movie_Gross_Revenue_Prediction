import json
import requests
from bs4 import BeautifulSoup 
from six.moves import urllib
import time
import os
import omdb

def getrevenuedata(ttnumber):
	#Budget,Opening Weekend,Number of Screens,Gross
	revenue
	URLrevenue = 'http://www.imdb.com/title/'+str(ttnumber)+'/business?ref_=tt_dt_bus'
	response = urllib.request.urlopen(URLrevenue)
	html = response.read()
	soup = BeautifulSoup(html,'html.parser')
	for h5 in soup.find_all('h5'):
		if 'Budget' in h5:
			getbudget = h5.next_sibling.strip()
			if getbudget.find('(') != -1:
				start = getbudget.find('(')
				getbudget = getbudget[0:start].strip()
			print getbudget

		if 'Opening Weekend' in h5:
			g = 0
			count = 0
			for i in h5.next_siblings:

				if g == 1:
					count = count + 1
				if i.find("Screens)") and count == 4:
					i = i.strip()
					start = str(i).find('(')+1
					end = str(i).find('S',start)
					getScreens = str(i)[start:end].strip()
					print getScreens
					break
				if i.find("(USA)") != -1 and i.find("$") != -1  and g ==0:
					g = 1
					f = 1
					#print '1'
					getopening = i.strip()
					getopening = getopening[:-1]
					print getopening

			#getopening = h5.next_sibling.strip()
			#print getopening
		if 'Gross' in h5:
			getgross = h5.next_sibling.strip()
			if getgross.find('(') != -1:
				start = getgross.find('(')
				getgross = getgross[0:start].strip()
			print getgross


		
	


def collectdata():
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
		Year= []
		metascore = []
		imdb_score = []
		popularity = []
		budget = []
		weekend = []
		gross = []
		filename = '../ttnumbers/'+'tt' + str(year)+'.txt'
		inputfile = open(filename, "r")

		#1st line
		line = inputfile.readline()

		while line:
			genre = []
			line = inputfile.readline()
			line = line.strip()

			omdbrequest = omdb.imdbid(line,timeout=5)

			#Add ttnumber
			ttnumbers.append(line)
			URLmod = URLtt + line + '/?ref_=nv_sr_1'
			print URLmod
			response = urllib.request.urlopen(URLmod)
			html = response.read()
			#print html
			soup = BeautifulSoup(html,'html.parser')
			#title.append(soup.title.string)
			
			#Add rating
			getrating = str(omdbrequest['rated'])
			print getrating
			contentrating.append(getrating)

			#Add title
			gettitle = str(omdbrequest['title'])
			print gettitle
			title.append(gettitle)

			#Add duration
			getruntime = str(omdbrequest['runtime'])
			print getruntime
			duration.append(getruntime)
			
			#Add year
			getyear = str(omdbrequest['year'])
			print getyear
			Year.append(str(getyear))

			#Add metascore
			getscor = str(omdbrequest['metascore'])
			print getscor
			metascore.append(getscor)


			#Add imdb_score
			getimdb_score = str(omdbrequest['imdb_rating'])
			print getimdb_score
			imdb_score.append(getimdb_score)


			#Add release date
			getdate =  str(omdbrequest['released'])
			print getdate
			releasedate.append(getdate)


			#Add popularity
			popular = soup.find_all('span',class_='subText')
			try:
				text2 = str(popular[2])
				start = text2.find('>')+1
				end =  text2.find('(',start)
				getpopular = text2[start:end].strip()
				print getpopular
				popularity.append(getpopular)
			except IndexError:
				text2 = 'null'
				popularity.append('empty')
				print 'empty'

				


			#Add revenue
			getrevenuedata(line)

			'''
			#Add budget
			div_search = soup.find_all('div',class_='txt-block')
			for i in div_search:
				if i.get_text().find('Budget') != -1:
					text = str(i).strip()
					start = text.find('$')
					end = text.find('<span',start)
					getbudget = text[start:end].strip() 
					print getbudget
					budget.append(getbudget)

				if i.get_text().find('Opening Weekend') != -1:
					text = str(i).strip()
					if text.find('$') != -1:
						start = text.find('$')
					else:
						start = text.find("SGD")

					end = text.find('<span',start)
					getweekend = text[start:end].strip()

					weekend_country = getweekend.split(' ')
					#print weekend_country
					#print weekend_country[0].strip()
					starting = str(weekend_country[0].strip())
					ending = str(weekend_country[len(weekend_country)-1].strip())
					#week = weekend_country[0].strip()
					#country_ = weekend_country[len(weekend_country)-1].strip()
					
					getweekend = starting+' '+ending
					print getweekend
					weekend.append(getweekend)

				if i.get_text().find('Gross') != -1:
					text = str(i).strip()
					start = text.find('$')
					end = text.find('<span',start)
					getgross = text[start:end].strip()

					start1 = text.find('>',end)+1
					end1 = text.find('<',start1)
					getcountry = text[start1:end1].strip()

					getgross = getgross + ' '+getcountry

					print getgross
					weekend.append(getweekend)



					'''
		


			#Add genre
			span = soup.find_all('div', class_='subtext')
			for i in span:
				rate = i.find_all('meta')
				f = 0

				'''
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
				
				'''
				'''
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
				'''
				setgenre = i.find_all('a')
				for j in setgenre:
					text = j.get('href')
					#print text
					if text.find('genre') != -1:
						print j.get_text().strip()
						genre.append(j.get_text)
					
					'''
					if text.find('releaseinfo') != -1:
						#print text
						print j.get_text().strip()
						releasedate.append(j.get_text())
					'''




					

			
			#print soup.title.string

		genres.append(genre)
		inputfile.close()



def main():
	collectdata()



if __name__=='__main__':
	main()
