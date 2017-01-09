
#Google API KEY : AIzaSyCJ9D_Lr-oJnniHZkKLFEMuzqurLUhB2Do
#Search Engine ID :  003810376591448609181:kqyshve45w0

import json
import requests
from bs4 import BeautifulSoup 
from six.moves import urllib
import time
import os
import omdb
import sys
import urllib2
def getgoogleurl(search):
   return 'http://www.ecosia.org/search?q='+urllib2.quote(search)+'&oq='+urllib2.quote(search)
   

def getrottentomato(ttnumber,outputdata,omdbrequest):
	#tomatoFresh
	#tomatoRotten,
	#tomatoMeter
	#tomatoRating
	#tomatoUserMeter
	#tomatoUserRating
	#tomatoUserReviews
	line = str(ttnumber)
	headers = {'User-agent':'Mozilla/11.0'}
	gettitle = omdbrequest['title']
	
	gettitle_ = ''
	for i in range(len(gettitle)):
		value = int(ord(gettitle[i]))
		if value > 128:
			continue
		else:
			gettitle_ = gettitle_ + gettitle[i]
		
	
	#print gettitle_
	gettitle = gettitle_

	#print omdbrequest['title']
	#print omdbrequest['year']
	search = gettitle + ' '+omdbrequest['year'] + ' ' +'rotten tomatoes'
	req = urllib2.Request(getgoogleurl(search),None,headers)
	site = None
	while site is None:
		try:
			site = urllib2.urlopen(req)
		except:
			pass
	
   	#print site
   	data = site.read()
   	#print data
   	site.close()
	html = data
	soup = BeautifulSoup(html,'html.parser')
	tomatoe_link = 'empty'
	for a in soup.find_all('a', href=True):
	    
	    if a['href'].find('url') and a['href'].find('rottentomatoes') != -1:
	    	if a['href'].find('&') != -1:
	    		start = a['href'].find('&')
	    		a['href'] = a['href'][:start]
	    	if a['href'].find('=') != -1:
	    		start = a['href'].find('=')+1
	    		a['href'] = a['href'][start:]

	    	tomatoe_link = a['href']
	    	break
	#print data
	if ttnumber == 'tt2446042':
		tomatoe_link = 'https://www.rottentomatoes.com/m/taken_3/' 

	if ttnumber == 'tt1700845':
		tomatoe_link = 'https://www.rottentomatoes.com/m/771357233/'

	if ttnumber == 'tt0199626':
		tomatoe_link = 'https://www.rottentomatoes.com/m/in_the_cut/'

	if ttnumber == 'tt0893382':
		tomatoe_link = 'https://www.rottentomatoes.com/m/shine_a_light/'

	if ttnumber == 'tt1314228':
		tomatoe_link = 'https://www.rottentomatoes.com/m/1213718-did_you_hear_about_the_morgans/'
		
		
		
	print tomatoe_link
	outputdata[line]['rotten_url'] = tomatoe_link
	response = None
	while response is None:
		try:
			response = urllib.request.urlopen(tomatoe_link)
		except:
			pass



	soup1 = BeautifulSoup(response,'html.parser')
	#print soup1.title.string


	#tomatoMeter
	tomatoMeter = 'empty'

	for i in soup1.find_all('span', class_ = "meter-value superPageFontColor"):
		tomatoMeter =  i.get_text()
		break

	outputdata[line]['tomatoMeter'] = tomatoMeter.strip()
	print tomatoMeter

	#tomatorating
	tomatoRating = 'empty'
	for i in soup1.find_all('div', class_ = 'superPageFontColor'):
		#print i
		start_ = str(i).find('</span>') + 7;
		end_  = str(i).find('/',start_);
		i = str(i)[start_:end_];
		i = i.strip();
		tomatoRating = str(i)
		break;

	outputdata[line]['tomatoRating'] = tomatoRating.strip()
	print tomatoRating

	#userMeter
	userMeter = 'empty'
	for i in soup1.find_all('div', class_ = 'meter-value'):
		userMeter = i.get_text().strip()
		break;

	outputdata[line]['userMeter'] = userMeter.strip()
	print userMeter

	#userrating and userreviews
	userrating = 'empty'
	userreviews = 'empty'
	for i in soup1.find_all('div', class_ = 'audience-info hidden-xs superPageFontColor'):
		val_ = i.get_text().strip()
		start_ = str(val_).find(':') + 1;
		start2_ = str(val_).find(':',start_) + 1
		end_ = str(val_).find("/",start_);
		userrating = str(val_)[start_:end_].strip()
		userreviews = (str)(val_)[start2_:].strip()
		break;
	print userrating
	print userreviews
	outputdata[line]['userrating'] = userrating.strip()
	outputdata[line]['userreviews'] = userreviews.strip()
	return outputdata


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


		

		#Add duration
		getruntime = str(omdbrequest['runtime'])
		outputdata[line]['runtime'] = getruntime
		#print getruntime
		
		
		#Add year
		getyear = str(omdbrequest['year'])
		outputdata[line]['year'] = getyear
		#print getyear
		

		#Add Rotten Tomato Ratings
		outputdata =  getrottentomato(line,outputdata,omdbrequest)
		'''
		#Add imdbvotes
		rotten_ = None
		while rotten_ is None:
			try:
				rotten_ = omdb.request(t=omdbrequest['title'], y=getyear, plot='full', tomatoes='true', timeout=5)
			except:
				pass
		
		#Get json
		rotten_response = json.loads(rotten_.text)
		
		#Add imdbvotes
		imdbVotes = rotten_response['imdbVotes']
		outputdata[line]['imdbVotes'] = imdbVotes

		#TomatoFresh
		tomatoFresh = rotten_response['tomatoFresh']
		outputdata[line]['tomatoFresh'] = tomatoFresh

		#TomatoRotten
		tomatoRotten = rotten_response['tomatoRotten']
		outputdata[line]['tomatoRotten'] = tomatoRotten


		#tomatoMeter
		tomatoMeter = rotten_response['tomatoMeter']
		outputdata[line]['tomatoMeter'] = tomatoMeter
		#tomatoRating
		tomatoRating = rotten_response['tomatoRating']
		outputdata[line]['tomatoRating'] = tomatoRating
		#tomatoUserMeter
		tomatoUserMeter = rotten_response['tomatoUserMeter']
		outputdata[line]['tomatoUserMeter'] = tomatoUserMeter
		#tomatoUserRating
		tomatoUserRating = rotten_response['tomatoUserRating']
		outputdata[line]['tomatoUserRating'] = tomatoUserRating
		#tomatoUserReviews
		tomatoUserReviews = rotten_response['tomatoUserReviews']
		outputdata[line]['tomatoUserReviews'] = tomatoUserReviews


		'''
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
	outfilename = '../output_rotten/'+str(year)+'/movies_'+str(year)+'_'+str(idlow)+'_'+str(idhigh)+'.json'
	with open(outfilename,'w') as jfout:
		json.dump(datadump,jfout)



if __name__=='__main__':
	main()
