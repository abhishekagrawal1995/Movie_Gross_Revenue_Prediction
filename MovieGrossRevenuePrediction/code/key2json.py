import json
import sys
def main():

	year = str(sys.argv[1])
	filename = '../ttnumbers/tt'+str(year)+'.txt'
	outjsonfile = '../ttnumbers/tt'+str(year)+'.json'
	cnt = 1
	keydict = {}

	with open(filename,'r') as fin:
		for line in fin:
			line = line.strip()
			keydict[cnt]= line
			cnt = cnt + 1

	print keydict

	with open(outjsonfile,'w') as jfout:
		json.dump(keydict,jfout)


	with open(outjsonfile,'r') as jfin:
		keys = json.load(jfin)

	#print keys['40.725382_-74.000101']
	print "done"

if __name__=='__main__':
	main()