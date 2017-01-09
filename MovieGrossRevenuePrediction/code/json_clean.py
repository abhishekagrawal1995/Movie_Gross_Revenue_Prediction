import json


def read_json():
	injson1 = 'bm2014.json'
	with open(injson1,'r') as jfin:
		data = json.load(jfin)


	count = 0
	total = 0
	for i in data['data']:
		total = total + 1
		budget = data['data'][i]['budget']
		gross = data['data'][i]['gross']
		if not budget == "N/A":
			print budget,gross
			
			count = count + 1


	print total
	print count
		



def main():
	read_json()




if __name__=="__main__":
    main()