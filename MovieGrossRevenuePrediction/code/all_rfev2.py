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
	PATH = "../output_rotten/csv_data_00_14/Music"+"_all.csv"
	datacollected = pd.read_csv(PATH)
	drop_list = []
	
	#Clean Data
	for index, row in datacollected.iterrows():
		
		if row['budget'] == 'empty' or row['Gross'] == 'empty' or row['Screens'] == 'empty' or row['OpeningWeekend'] == 'empty' or row['popularity'] == 'empty' or row['tomatoMeter']=='empty' or row['tomatoRating'] == 'empty':
			drop_list.append(index)
	
	
	datacollected = datacollected.drop(datacollected.index[drop_list])

	df = datacollected
	#print datacollected
	feature_names = ["budget","imdb_rating","metascore","OpeningWeekend","popularity","Screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]
	feature_names = np.asarray(feature_names)
	X = df[["budget","imdb_rating","metascore","OpeningWeekend","popularity","Screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]]
	Y = df.Gross
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
	 
	
	rlasso = RandomizedLasso(alpha=0.04)
	rlasso.fit(X, Y)
	ranks["RandomLasso"] = rank_to_dict(np.abs(rlasso.scores_), names)
		 

	'''	 
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