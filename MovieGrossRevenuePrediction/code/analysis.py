import json
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib
import pylab
import sys
import numpy
plt.switch_backend('agg')

#Get Parameters to Plot
def getparameters(data):
	budget_gross = {}
	xaxis = []
	yaxis = []

	for key, value in data.iteritems():
			budget_ = data[key]['userreviews']
			budget_ = str(budget_).replace('N','empty').strip()
			gross_ = data[key]['Gross']
			if budget_.find('empty') == -1 and gross_.find('empty') == -1:
				#budget_gross[budget_] = gross_
				xaxis.append(budget_)
				yaxis.append(gross_)
				
	#xaxis.sort()				
	#for i in xaxis:
		#yaxis.append(budget_gross[i])
	xxaxis = list()
	yyaxis = list()
	for i in range(len(xaxis)):
		xxaxis.append(float(xaxis[i]))
	for i in range(len(yaxis)):
		yyaxis.append(float(yaxis[i]))
	
	print numpy.corrcoef(xxaxis,yyaxis)
	return [xaxis,yaxis]

def main():

	#year = str(sys.argv[1])
	font = {'weight' : 'bold'}
	matplotlib.rc('font', **font)
	data = {}
	startyear = 2000
	endyear = 2015
	while startyear <=endyear:
		inf= '../output_rotten/'+str(startyear)+'/movies_merge_clean_inflation_'+str(startyear)+'.json'
		with open(inf,'r') as jfin:
			data1 = json.load(jfin)
		startyear = startyear + 1
		for key,value in data1.iteritems():
			data[key] = data1[key]

	

	diff_dict = {0:'Analyse'}
	colors = {0:'red'}

	fig = plt.figure() 
	ax = fig.add_subplot(111)
	red_patch1 = mpatches.Patch(color='red', label='Analyse')


	#ax.set_ylim([0.0,1])
	[xaxis,yaxis] = getparameters(data)
	#print xaxis
	#print yaxis
	#plt.plot(xaxis,yaxis,'ro',color = colors[0])
		
		

	
	plt.legend(handles=[red_patch1],loc = 2)
	fig.suptitle('Screens vs Gross',fontsize = 20,fontweight='bold')
	ax.set_xlabel('Budget(USD)',fontsize = 10,fontweight='bold')
	ax.set_ylabel('Gross(USD)',fontsize = 10,fontweight='bold')	
	#plt.tight_layout()
	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
		item.set_fontsize(15) 

	#pylab.tight_layout()    
	fig.savefig('../output/pdf/'+'Screens_gross_'+str(year)+'.pdf')
			


if __name__=='__main__':
	main()