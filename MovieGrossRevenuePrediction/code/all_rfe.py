from sklearn.datasets import load_boston
from sklearn.linear_model import (LinearRegression, Ridge, 
                                  Lasso, RandomizedLasso)
from sklearn.feature_selection import RFE, f_regression
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from minepy import MINE
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

	
def rank_to_dict(ranks, names, order=1):
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(order*np.array([ranks]).T).T[0]
    ranks = map(lambda x: round(x, 2), ranks)
    return dict(zip(names, ranks ))

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
	feature_names = ["budget","imdb_rating","metascore","opening_weekend","popularity","screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]
	feature_names = np.asarray(feature_names)
	X = df[["budget","imdb_rating","metascore","opening_weekend","popularity","screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]]
	Y = df.gross
	X = X.astype(float) 
	Y = Y.astype(float) 
	names = feature_names

	ranks = {}
 

 	'''
	lr = LinearRegression(normalize=True)
	lr.fit(X, Y)
	ranks["Linear reg"] = rank_to_dict(np.abs(lr.coef_), names)
	 '''
	ridge = Ridge(alpha=7)
	ridge.fit(X, Y)
	ranks["Ridge"] = rank_to_dict(np.abs(ridge.coef_), names)
	 
	 
	lasso = Lasso(alpha=.05)
	lasso.fit(X, Y)
	ranks["Lasso"] = rank_to_dict(np.abs(lasso.coef_), names)
	 
	'''
	rlasso = RandomizedLasso(alpha=0.04)
	rlasso.fit(X, Y)
	ranks["Stability"] = rank_to_dict(np.abs(rlasso.scores_), names)
		 
	#stop the search when 5 features are left (they will get equal scores)
	rfe = RFE(lr, n_features_to_select=5)
	rfe.fit(X,Y)
	ranks["RFE"] = rank_to_dict(map(float, rfe.ranking_), names, order=-1)
	 
	rf = RandomForestRegressor()
	rf.fit(X,Y)
	ranks["RF"] = rank_to_dict(rf.feature_importances_, names)
	 
	 
	f, pval  = f_regression(X, Y, center=True)
	ranks["Corr."] = rank_to_dict(f, names)
	 
	
	mine = MINE()
	mic_scores = []
	for i in range(X.shape[1]):
	    #mine.compute_score(X[:,i], Y)
	    #m = mine.mic()
	    mic_scores.append('0.0')
	 
	ranks["MIC"] = rank_to_dict(mic_scores, names) 
	 
	 '''
	r = {}
	for name in names:
	    r[name] = round(np.mean([ranks[method][name] 
	                             for method in ranks.keys()]), 2)
	 
	methods = sorted(ranks.keys())
	ranks["Mean"] = r
	methods.append("Mean")
	
	print "\t%s" % "\t".join(methods)
	for name in names:
	    print "%s\t%s" % (name, "\t".join(map(str,[ranks[method][name] for method in methods])))



if __name__=='__main__':
	main()