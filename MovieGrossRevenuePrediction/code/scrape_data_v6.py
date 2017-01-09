import json
import requests
from bs4 import BeautifulSoup 
from six.moves import urllib
import time
import os
import omdb
import sys

def getrevenuedata(ttnumber,outputdata):
	#Budget,Opening Weekend,Number of Screens,Gross revenue
	URLrevenue = 'http://www.imdb.com/title/'+str(ttnumber)+'/business?ref_=tt_dt_bus'
	response = None
	while response is None:
			try:
				response = urllib.request.urlopen(URLrevenue)
			except:
				pass
	

	line = str(ttnumber)
	html = response.read()
	soup = BeautifulSoup(html,'html.parser')

	getbudget = 'empty'

	getopening = 'empty'
	getScreens = 'empty'
	getgross = 'empty'
	for h5 in soup.find_all('h5'):
		
		if 'Budget' in h5:
			getbudget = h5.next_sibling.strip()
			if getbudget.find('(') != -1:
				start = getbudget.find('(')
				getbudget = getbudget[0:start].strip()
			outputdata[line]['budget'] = getbudget
		
		if 'Opening Weekend' in h5:
			g = 0
			count = 0
			for i in h5.next_siblings:

				if i.encode('utf-8').find('Gross') != -1:
					break
				if g == 1:
					count = count + 1

				if i.encode('utf-8').find("Screens") and count == 4:
					i = i.strip()
					start = str(i).find('(')+1
					end = str(i).find('S',start)
					getScreens = str(i)[start:end].strip()
					break
				
					
				if i.encode('utf-8').find("(USA)") != -1 and i.find("$") != -1  and g ==0:
					g = 1
					f = 1
					#print i
					
					getopening = i.strip()
					getopening = getopening[:-1]
				
					#print getopening,"Opening"


			if getopening.find('empty') != -1:
				outputdata[line]['OpeningWeekend'] ='empty'
			else:
				outputdata[line]['OpeningWeekend'] = getopening
			if getScreens.find('empty') != -1:
				outputdata[line]['Screens'] = 'empty'
			else:
				outputdata[line]['Screens'] =getScreens
			#print getScreens,"Screens"

			#getopening = h5.next_sibling.strip()
			#print getopening
		if 'Gross' in h5:
			getgross = h5.next_sibling.strip()
			if getgross.find('(') != -1:
				start = getgross.find('(')
				getgross = getgross[0:start].strip()
			outputdata[line]['Gross'] = getgross.strip()

		
		
			
			


	#Set Budget check
	if getbudget.find('empty') != -1:
		outputdata[line]['budget'] = 'empty'
		
	#print getbudget,"Budget"

	if getgross.find('empty') != -1:
			outputdata[line]['Gross'] ='empty'
	#print outputdata
	return outputdata

def collectdata(keys,idlow,idhigh,year):

	URLtt = 'http://www.imdb.com/title/'
	#Animation,Action,Adventure,Horror,Family,Drama,Biography,Comedy,Sci-Fi,Crime,Mystery,Documentary
	
	outputdata = {}

	low = idlow
	while low <= idhigh:
		outputdata[keys[str(low)]] = {}
		low = low + 1

	low = idlow	
	while low <= idhigh:

		line = keys[str(low)]

		print line
		#Make Request
		omdbrequest = None
		while omdbrequest is None:
			try:
				omdbrequest = omdb.imdbid(line,timeout=10)
			except:
				pass
		

		#Add ttnumber
		
		URLmod = URLtt + line + '/?ref_=nv_sr_1'
		outputdata[line]['url'] = URLmod
		#print URLmod

		response = None
		while response is None:
			try:
				response = urllib.request.urlopen(URLmod)
			except:
				pass
	
		html = response.read()
		#print html
		soup = BeautifulSoup(html,'html.parser')
		#title.append(soup.title.string)
		
		#Add rating
		getrating = str(omdbrequest['rated'])
		outputdata[line]['contentrating'] = getrating
		#print getrating
		
		
		#Add title
		gettitle = omdbrequest['title']
		#print gettitle
		outputdata[line]['title'] = gettitle

		#print gettitle
		

		#Add duration
		getruntime = str(omdbrequest['runtime'])
		outputdata[line]['runtime'] = getruntime
		#print getruntime
		
		
		#Add year
		getyear = str(omdbrequest['year'])
		outputdata[line]['year'] = getyear
		#print getyear
		

		#Add metascore
		getscor = str(omdbrequest['metascore'])
		outputdata[line]['metascore'] = getscor
		#print getscor
		


		#Add imdb_score
		getimdb_score = str(omdbrequest['imdb_rating'])
		outputdata[line]['imdb_rating'] = getimdb_score
		#print getimdb_score
	


		#Add release date
		getdate =  str(omdbrequest['released'])
		outputdata[line]['releasedate'] = getdate
		#print getdate
		


		#Add popularity
		popular = soup.find_all('span',class_='subText')
		try:
			text2 = str(popular[2])
			start = text2.find('>')+1
			end =  text2.find('(',start)
			getpopular = text2[start:end].strip()
			#print getpopular
			outputdata[line]['popularity'] = getpopular
			
		except IndexError:
			text2 = 'null'
			
			outputdata[line]['popularity'] = 'empty'
			#print 'empty'

		#Add revenue
		outputdata =  getrevenuedata(line,outputdata)


		#Add genre
		span = soup.find_all('div', class_='subtext')
		genre = []
		for i in span:
			rate = i.find_all('meta')
			f = 0
			setgenre = i.find_all('a')
			for j in setgenre:
				text = j.get('href')
				#print text
				if text.find('genre') != -1:
					#print j.get_text().strip()
					genre.append(j.get_text().strip())

		outputdata[line]['Genre'] = genre

		low = low + 1
		
	
	return outputdata		
			
def main():
	
	year = str(sys.argv[1])
	idlow = int(sys.argv[2])
	idhigh = int(sys.argv[3])

	outjsonfile = '../ttnumbers/tt'+str(year)+'.json'

	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	datadump = collectdata(keys,idlow,idhigh,year)
	
	#Writing the result to a json file 
	outfilename = '../output/'+str(year)+'/movies_'+str(year)+'_'+str(idlow)+'_'+str(idhigh)+'.json'
	with open(outfilename,'w') as jfout:
		json.dump(datadump,jfout)



if __name__=='__main__':
	main()
