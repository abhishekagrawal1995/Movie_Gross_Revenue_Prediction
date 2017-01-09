from sklearn.linear_model import Lasso
import numpy
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import pandas as pd
import json
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import math
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import KFold
import sys
import os
from sklearn.svm import SVR




def main():
	genre_ = ['Action','Adventure','Animation','Comedy','Crime','Horror','Documentary','Biography','Drama','Romance','Sci-Fi','Thriller','Family','Fantasy','History','Mystery','Sport','Music']
	combination = {'Mystery': [0, 1, 4, 10], 'Romance': [0, 1, 10], 'Sport': [0, 1, 3, 4, 6, 7], 'Sci-Fi': [1], 'Family': [0, 1, 4, 7, 10], 'Horror': [1, 10], 'Thriller': [0, 1], 'Crime': [0, 1], 'Drama': [0, 1, 4], 'Fantasy': [0, 1, 2, 4, 9], 'Animation': [0, 1], 'Music': [0, 1, 6, 10], 'Adventure': [0, 1], 'Action': [1,4], 'Comedy': [0, 1], 'Documentary': [4, 7, 9, 10], 'Biography': [0, 1, 3, 4, 6, 7], 'History': [1, 4, 7]}
	features_Set = {0:'budget',1:'OpeningWeekend',2:'Screens',3:'metascore',4:'popularity',5:'imdb_rating',6:'tomatoMeter',7:'tomatoRating',8:'userMeter',9:'userrating',10:'userreviews',11:'Gross'}
	for genre in genre_:
		PATH = "../output_rotten/csv_data_00_14/"+genre+"_all.csv"
		datacollected = pd.read_csv(PATH)
		drop_list = []
		for index, row in datacollected.iterrows():
			if row['budget'] == 'empty' or row['Gross'] == 'empty' or row['Screens'] == 'empty' or row['OpeningWeekend'] == 'empty' or row['popularity'] == 'empty' or row['tomatoMeter']=='empty' or row['tomatoRating'] == 'empty':
				drop_list.append(index)


		datacollected = datacollected.drop(datacollected.index[drop_list])
		
		best_comb = combination[genre] 
		features_list = []
		for i in best_comb:
			features_list.append(features_Set[i])
		features = datacollected[features_list]
		targetVariables =  datacollected.Gross
		featureTrain,featuresTest,targetTrain,targetTest = train_test_split(features,targetVariables,test_size = 0.20)
		regr = linear_model.LinearRegression()
		regr.fit(featureTrain, targetTrain)
		predictions = regr.predict(featuresTest)
		target = list(targetTest)
		predictions = list(predictions)
		for i in range(len(target)):
			target[i] =  float(target[i])

		r2_score_linear = r2_score(target, predictions)

		print genre,r2_score_linear
		





if __name__=='__main__':
	main()