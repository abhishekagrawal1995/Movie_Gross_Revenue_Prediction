import json
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib
import pylab
import sys
plt.switch_backend('agg')

#Get Parameters to Plot


def set_prices(prices):
	prices['2000'] = '5.39'
	prices['2001'] = '5.66'
	prices['2002'] = '5.81'
	prices['2003'] = '6.03'
	prices['2004'] = '6.21'
	prices['2005'] = '6.41'
	prices['2006'] = '6.55'
	prices['2007'] = '6.88'
	prices['2008'] = '7.18'
	prices['2009'] = '7.50'
	prices['2010'] = '7.89'
	prices['2011'] = '7.93'
	prices['2012'] = '7.96'
	prices['2013'] = '8.13'
	prices['2014'] = '8.17'
	prices['2015'] = '8.43'
	prices['2016'] = '8.66'

	return prices

def getparameters(prices):
	budget_gross = {}
	xaxis = []
	yaxis = []

	for key, value in prices.iteritems():
		xaxis.append(key)
		yaxis.append(prices[key])
		
	return [xaxis,yaxis]

def main():

	prices = {}
	prices = set_prices(prices)

	font = {'weight' : 'bold'}
	matplotlib.rc('font', **font)

	diff_dict = {0:'Prices'}
	colors = {0:'red'}

	fig = plt.figure() 
	ax = fig.add_subplot(111)
	red_patch1 = mpatches.Patch(color='red', label='Prices')


	#ax.set_ylim([0,500000000])
	[xaxis,yaxis] = getparameters(prices)
	print xaxis
	print yaxis
	plt.plot(xaxis,yaxis,'ro',color = colors[0])
		
		

	plt.legend(handles=[red_patch1],loc = 4)
	#fig.suptitle('Hour 20',fontsize = 20,fontweight='bold')
	ax.set_xlabel('Year',fontsize = 20,fontweight='bold')
	ax.set_ylabel('Movie Ticket Price(USD)',fontsize = 20,fontweight='bold')	
	#plt.tight_layout()
	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
		item.set_fontsize(20) 

	#pylab.tight_layout()    
	fig.savefig('../output/pdf/'+'movie_ticket_price'+'.png')

			


if __name__=='__main__':
	main()