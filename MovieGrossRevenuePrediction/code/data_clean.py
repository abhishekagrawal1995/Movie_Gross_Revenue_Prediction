# -*- coding: iso-8859-15 -*-
import json
import gzip
import sys

#Animation,Action,Adventure,Horror,Family,Drama,Biography,Comedy,Sci-Fi,Crime,Mystery,Documentary

def main():
	#Input Year
	year = str(sys.argv[1])
	infilename = '../output/'+str(year)+'/movies_merge_'+str(year)+'.json'
	outfilename = '../output/'+str(year)+'/movies_merge_clean_'+str(year)+'.json'
	with open(infilename,'r') as jfin:
		keys = json.load(jfin)

	for key, value in keys.iteritems():
		#keys['tt1741225']['OpeningWeekend'] = "$39,690 (USA)"
		
		#Gross_clean
		gross_  = keys[key]['Gross']
		gross_ = gross_.replace('$','')
		gross_ = gross_.replace(',','')
		#print gross_
		if gross_.find('empty') == -1:
			#print key,gross_
			value = int(ord(gross_[0]))
			
			if value == 163:
				gross_ = gross_[1:].strip()
				gross_n = long(gross_)*1.33
				gross_ = str(int(gross_n))
				
			#gross_ = inflation(prices,current_year,year,gross_)
		keys[key]['Gross'] = gross_

		#Opening_Weekend_Revenue
		if keys[key].has_key("OpeningWeekend"):
		

			if keys[key]['OpeningWeekend'].find('empty') == -1:
				weekend_ = keys[key]['OpeningWeekend']
				weekend_ = weekend_.replace(',','')
				end = weekend_.find('(')
				start = weekend_.find('$')+1
				weekend_ = weekend_[start:end].strip()
				keys[key]['OpeningWeekend'] = weekend_
				#print weekend_ 
		else:
			keys[key]['OpeningWeekend'] ='empty'
			#keys['tt1741225']['OpeningWeekend'] = "39690"
		
		#Budget_clean
		euro = u"€"
		pound = u"£"


		budget_  = keys[key]['budget']
		budget_ = budget_.replace(',','')
		if budget_.find('$CAD') != -1:
			budget_ = budget_.replace('$CAD', '').strip()
			budget_n = long(budget_) * 0.76
			budget_ = str(long(budget_n))
		elif budget_.find('$') != -1:
			#print key,budget_
			budget_ = budget_.replace('$','').strip()
		elif budget_.find('FRF') != -1:
			#print key,budget_
			budget_ = budget_.replace('FRF','').strip()
			budget_n = long(budget_)*0.171102
			budget_ = str(long(budget_n))
		elif budget_.find('ATS') != -1:
			#print key,budget_
			budget_ =  budget_.replace('ATS','').strip()
			budget_n = long(budget_)*0.0815626
			budget_ = str(long(budget_n))
		elif budget_.find('INR') != -1:
			#print key,budget_
			budget_ =  budget_.replace('INR','').strip()
			budget_n = long(budget_)*0.015
			budget_ = str(long(budget_n))
		elif budget_.find('NZD') != -1:
			#print key,budget_
			budget_ =  budget_.replace('NZD','').strip()
			budget_n = long(budget_)*0.73
			budget_ = str(long(budget_n))
		elif budget_.find('DKK') != -1:
			#print key,budget_
			budget_ =  budget_.replace('DKK','').strip()
			budget_n = long(budget_)*0.15
			budget_ = str(long(budget_n))
		elif budget_.find('CNY') != -1:
			#print key,budget_
			budget_ =  budget_.replace('CNY','').strip()
			budget_n = long(budget_)*0.15
			budget_ = str(long(budget_n))
		elif budget_.find('THB') != -1:
			#print key,budget_
			budget_ =  budget_.replace('THB','').strip()
			budget_n = long(budget_)*0.029
			budget_ = str(long(budget_n))
		elif budget_.find('AUD') != -1:
			#print key,budget_
			budget_ =  budget_.replace('AUD','').strip()
			budget_n = long(budget_)*0.75
			budget_ = str(long(budget_n))
		elif budget_.find('HUF') != -1:
			#print key,budget_
			budget_ =  budget_.replace('HUF','').strip()
			budget_n = long(budget_)*0.0036
			budget_ = str(long(budget_n))
		

		else:
			if budget_.find('empty') == -1:
				#print key,budget_
				
				value = int(ord(budget_[0]))
				#print value
				budget_ = budget_[1:].strip()
				if value == 163:
					budget_n = long(budget_)*1.33
					budget_ = str(int(budget_n))

				if value == 8364:
					budget_n = long(budget_)*1.12
					budget_ = str(int(budget_n))
				#print key,budget_
		
			
		
		#put budget
		keys[key]['budget'] = budget_

		#Popularity_clean
		popularity_ = keys[key]['popularity']
		popularity_ = popularity_.replace(',','')
		keys[key]['popularity'] = popularity_
		#print popularity_
		#Screens_clean
		if keys[key].has_key('Screens'):
			screen_ = keys[key]['Screens']
			screen_ = screen_.replace(',','')
			keys[key]['Screens'] = screen_
			#print screen_
		else:
			keys[key]['Screens'] = 'empty'


	with open(outfilename,'w') as jfout:
		json.dump(keys,jfout)


if __name__=='__main__':
	main()