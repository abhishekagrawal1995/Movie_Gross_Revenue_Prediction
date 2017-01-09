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
	PATH = "../output_rotten/csv_data_00_14/Adventure"+"_all.csv"
	datacollected = pd.read_csv(PATH)
	drop_list = []
	
	#Clean Data
	for index, row in datacollected.iterrows():
		
		if row['budget'] == 'empty' or row['Gross'] == 'empty' or row['Screens'] == 'empty' or row['OpeningWeekend'] == 'empty' or row['popularity'] == 'empty' or row['tomatoMeter']=='empty' or row['tomatoRating'] == 'empty':
			drop_list.append(index)
	
	
	datacollected = datacollected.drop(datacollected.index[drop_list])
	df = datacollected
	
	
	
	#print datacollected
	feature_names_ = ["budget","imdb_rating","metascore","OpeningWeekend","popularity","Screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]
	feature_names_ = np.asarray(feature_names_)
	X = df[["budget","imdb_rating","metascore","OpeningWeekend","popularity","Screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]]
	Y = df.Gross
	X = X.astype(float) 
	Y = Y.astype(float) 
	names = feature_names_
 	regr = linear_model.LinearRegression()
 	rfe = RFE(regr, n_features_to_select=3)
	rfe.fit(X,Y)
 
	print "Features sorted by their rank:"
	print sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), names))
	print(rfe.support_)

	


if __name__=='__main__':
	main()