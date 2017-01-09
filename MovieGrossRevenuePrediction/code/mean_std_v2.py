import numpy
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import pandas as pd
import json
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import math
from sklearn.cross_validation import KFold
import sys
import os

def main():
	inputfilename = '../output_rotten/'+'/movies_merge_clean_inflation_all'+'.json'
	outfilename = '../output_rotten/'+'/mean_std_h'+'.json'
	with open(inputfilename,'r') as jfin:
		inp = json.load(jfin)


	features_Set = {0:'budget',1:'OpeningWeekend',2:'Screens',3:'metascore',4:'popularity',5:'imdb_rating',6:'tomatoMeter',7:'tomatoRating',8:'userMeter',9:'userrating',10:'userreviews',11:'Gross'}

	mean_std = {}

	for i in range(0,12):
		mean_std[features_Set[i]] = {}

	for i in range(0,12):
		mean_std[features_Set[i]]['sum'] = 0
		mean_std[features_Set[i]]['squaredsum'] = 0
		mean_std[features_Set[i]]['mean'] = 0
		mean_std[features_Set[i]]['count'] = 0
		mean_std[features_Set[i]]['std'] = 0
	
	for key, value in inp.iteritems():

		for i in range(0,12):
			x = inp[key][features_Set[i]]
			if x != 'empty' and x != 'N/A' and x != 'N':
				rating = inp[key][features_Set[7]]
				if rating != 'empty':
					if float(rating) > 5.0:
						#print rating
						mean_std[features_Set[i]]['count'] = mean_std[features_Set[i]]['count'] + 1
						mean_std[features_Set[i]]['sum'] = mean_std[features_Set[i]]['sum'] + float(x)
						mean_std[features_Set[i]]['squaredsum'] = mean_std[features_Set[i]]['squaredsum'] + float(x)*float(x)


	for i in range(0,12):
		mean_std[features_Set[i]]['mean'] = mean_std[features_Set[i]]['sum'] / mean_std[features_Set[i]]['count']
		mean_std[features_Set[i]]['std'] = math.sqrt((mean_std[features_Set[i]]['squaredsum']/mean_std[features_Set[i]]['count'])-(mean_std[features_Set[i]]['mean'])*(mean_std[features_Set[i]]['mean']))
	
	#print mean_std


	with open(outfilename,'w') as jfout:
		json.dump(mean_std,jfout)

if __name__=='__main__':
	main()