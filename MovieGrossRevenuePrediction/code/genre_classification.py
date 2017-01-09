import json
import gzip
import sys

def main():
	#Input Year
	year = str(sys.argv[1])

	#genre will store all types of genres movies are of
	genre = {}

	#genre_data will store the key:value with key as type of genre and value as ttnumber of the movie
	genre_data = {}


	#Inputfile
	filename = '../output_rotten/'+str(year)+'/movies_merge_clean_inflation_'+str(year)+'.json'

	
	#Load the file
	with open(filename,'r') as jfin:
		keys = json.load(jfin)
	
	#Find all types of genre that exist
	for key, value in keys.iteritems():
			genre_list = keys[key]['Genre']
			for l in genre_list:
				genre[l] = 1



	#Make a list  of them all
	genre_list = list()
	for key, value in genre.iteritems():
		#print key
		genre_list.append(key)

	#Create an empty dictionary
	for i in genre_list:
		genre_data[i] = list() 
	

	#Add add one by one to each of the category movie belongs
	for key, value in keys.iteritems():
		genre_list = keys[key]['Genre']
		for l in genre_list:
			genre_data[l].append(key)


	#Now make files and dump them
	for key, value in genre.iteritems():
		filename = '../output_rotten/'+str(year)+'/Genre_inflation/'+str(key)+'_'+str(year)+'.json' 
		datadump = {}
		tt_list = genre_data[key]

		for i in tt_list:
			datadump[str(i)]=keys[i]
		
		with open(filename,'w') as jfout:
			json.dump(datadump,jfout)

	#print genre_data








	



if __name__=='__main__':
	main()