import json
import gzip
import sys

def main():
	year = str(sys.argv[1])
	intials = 'movies_'+str(year)
	dict_10 = {}

	begin = 1
	window = 10

	for i in range(1,21):
		
		startid = begin
		endid = startid + window - 1

		filename = '../output_rotten/'+str(year)+'/'+intials+'_'+str(startid)+'_'+str(endid)+'.json'
		print filename
		with open(filename,'r') as jfin:
			keys = json.load(jfin)
			#print keys
		for key, value in keys.iteritems():
			dict_10[key] = value

		begin = endid+1

	
	#Writing the result to a json file 
	outfilename = '../output_rotten/'+str(year)+'/movies_merge_clean_inflation_'+str(year)+'.json'
	with open(outfilename,'w') as jfout:
		json.dump(dict_10,jfout)



if __name__=='__main__':
	main()