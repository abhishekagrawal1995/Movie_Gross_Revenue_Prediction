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
			budget_ = data[key]['imdb_rating']
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
		#print xaxis[i]
		xxaxis.append(float(xaxis[i]))
	for i in range(len(yaxis)):
		yyaxis.append(float(yaxis[i]))
	
	print numpy.corrcoef(xxaxis,yyaxis)
	return [xaxis,yaxis]

def main():

	
	font = {'weight' : 'bold'}
	matplotlib.rc('font', **font)
	genre_ = ['Action','Adventure','Animation','Comedy','Crime','Horror','Documentary','Biography','Drama','Romance','Sci-Fi','Thriller','Family','Fantasy','History','Mystery','Sport','Music']
	
	for gen in genre_:
		data = {}
		startyear = 2000
		endyear = 2015
		while startyear <=endyear:
			inf= '../output/'+str(startyear)+'/Genre_inflation/'+str(gen)+'_'+str(startyear)+'.json'
			with open(inf,'r') as jfin:
				data1 = json.load(jfin)

			for key,value in data1.iteritems():
				#if data1[key]['popularity'].find('</span') != -1:
					#print key,startyear
				data[key] = data1[key]

			startyear = startyear + 1
		print gen 
		[xaxis,yaxis] = getparameters(data)


	diff_dict = {0:'Analyse'}
	colors = {0:'red'}

	fig = plt.figure() 
	ax = fig.add_subplot(111)
	red_patch1 = mpatches.Patch(color='red', label='Analyse')


	#ax.set_ylim([0,500000000])
	#[xaxis,yaxis] = getparameters(data)
	#print xaxis
	#print yaxis
	#plt.plot([1, 2, 3, 4], [1, 4, 9, 16],color = colors[0])
	#plt.plot(xaxis,yaxis,'ro',color = colors[0])
		
		

	plt.legend(handles=[red_patch1],loc = 2)
	fig.suptitle('Screens vs Gross',fontsize = 20,fontweight='bold')
	ax.set_xlabel('Budget(USD)',fontsize = 10,fontweight='bold')
	ax.set_ylabel('Gross(USD)',fontsize = 10,fontweight='bold')	
	#plt.tight_layout()
	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
		item.set_fontsize(15) 

	#pylab.tight_layout()    
	fig.savefig('../output/pdf/'+'Screens_gross_all'+'.pdf')

			


if __name__=='__main__':
	main()