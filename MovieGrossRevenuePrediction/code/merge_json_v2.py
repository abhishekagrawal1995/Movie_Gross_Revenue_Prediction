import json
import gzip
import sys

def main():
	
	startyear = 2013
	endyear = 2015
	dict_10 = {}

	while startyear <= endyear:
		filename = '../output_rotten/'+str(startyear)+'/movies_merge_clean_inflation_'+str(startyear)+'.json'
		print filename
		with open(filename,'r') as jfin:
			keys = json.load(jfin)
			#print keys
		for key, value in keys.iteritems():
			dict_10[key] = value

		startyear = startyear + 1

	
	#Writing the result to a json file 
	outfilename = '../output_rotten/'+'/movies_merge_clean_inflation_2013_15'+'.json'
	with open(outfilename,'w') as jfout:
		json.dump(dict_10,jfout)



if __name__=='__main__':
	main()