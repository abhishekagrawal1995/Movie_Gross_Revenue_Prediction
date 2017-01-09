from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
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
	PATH = "../output_rotten/csv_data/Action"+"_all.csv"
	datacollected = pd.read_csv(PATH)
	drop_list = []
	
	#Clean Data
	for index, row in datacollected.iterrows():
		
		if row['budget'] == 'empty' or row['gross'] == 'empty' or row['screens'] == 'empty' or row['opening_weekend'] == 'empty' or row['popularity'] == 'empty' or row['tomatoMeter']=='empty' or row['tomatoRating'] == 'empty':
			drop_list.append(index)
	
	
	datacollected = datacollected.drop(datacollected.index[drop_list])

	df = datacollected
	df = df[df.budget == '0']
	#print df

	
	feature_names = ["budget","gross","imdb_rating","metascore","opening_weekend","popularity","screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]
	
	min_max_map = {}
	for feature in feature_names:
		min_max_map[feature] = {}

	for feature in feature_names:
		min_max_map[feature]['mini'] = 0
		min_max_map[feature]['maxi'] = 0

	for feature in feature_names:
		feature_  = datacollected[feature].tolist()
		for i, val in enumerate(feature_):
			feature_[i] = float(feature_[i])
		
		min_max_map[feature]['maxi'] = max(feature_)
		min_max_map[feature]['mini'] = min(feature_)
		

	min_max_map['imdb_rating']['mini'] = 0
	min_max_map['imdb_rating']['maxi'] = 10
	min_max_map['metascore']['mini'] = 0
	min_max_map['metascore']['maxi'] = 100

	min_max_map['tomatoMeter']['mini'] = 0
	min_max_map['tomatoMeter']['maxi'] = 100

	min_max_map['tomatoRating']['mini'] = 0
	min_max_map['tomatoRating']['maxi'] = 10

	min_max_map['userrating']['mini'] = 0
	min_max_map['userrating']['maxi'] = 5

	min_max_map['userMeter']['mini'] = 0
	min_max_map['userMeter']['maxi'] = 100


	print min_max_map
	for index,row in datacollected.iterrows():
		for feature in feature_names:
			x = row[feature]
			x = float(x)
			m = float(min_max_map[feature]['mini'])
			mm = float(min_max_map[feature]['maxi'])
			if m == mm:
				m = mm-0.1
			y = (float)(x - m)
		
			y = (float)(y/(mm-m))
			y = y *100
			#print y
			row[feature] = str(y)
		df.loc[-1] = row
		df.index = df.index + 1  # shifting index
 		df = df.sort() 

		
			

	#print datacollected
	#print df
	
	

	#print min_max_map
	#print datacollected


	
	#print datacollected
	feature_names_ = ["budget","imdb_rating","metascore","opening_weekend","popularity","screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]
	feature_names_ = np.asarray(feature_names_)
	X = df[["budget","imdb_rating","metascore","opening_weekend","popularity","screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]]
	Y = df.gross
	X = X.astype(float) 
	Y = Y.astype(float) 
	names = feature_names_
 	regr = linear_model.LinearRegression()
 	rfe = RFE(regr, n_features_to_select=1)
	rfe.fit(X,Y)
 
	print "Features sorted by their rank:"
	print sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), names))
	print(rfe.support_)

	


if __name__=='__main__':
	main()