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


def mse(est,real):
	e = est
	r = real
	#diff = set(list(abs(r-e)))
	#print sorted(diff)
	rr = []
	ee = []
	dd = list(abs(np.array(r)-np.array(e)))
	

	for i in xrange(len(dd)):
		rr.append(r[i])
		ee.append(e[i])
			

	rr = np.array(rr)
	ee = np.array(ee)

	mse = sum((rr-ee)*(rr-ee))/len(rr)
	return mse
def main():
	
		PATH = '../output_rotten/csv_data/'+'genre_predicted_value'+'_all.csv'
		
		datacollected = pd.read_csv(PATH)
		
		total_items = len(datacollected.index)

		#print datacollected
		
		kf = KFold(total_items, n_folds=10)
		mean_ = []
		gross_ = list(datacollected.gross)
		Gr = []
		for i in range(len(gross_)):
			if gross_[i] != 'empty':
				Gr.append(float(gross_[i]))

		me = np.mean(Gr)
		for train_index, test_index in kf:
			
			Train,Test = datacollected.iloc[train_index],datacollected.iloc[test_index]
			featureTrain = Train[['Action','Adventure','Animation','Comedy','Crime','Horror','Documentary','Biography','Drama','Romance','Sci-Fi','Thriller','Family','Fantasy','History','Mystery','Sport','Music']]

			targetTrain = Train.gross
			featuresTest = Test[['Action','Adventure','Animation','Comedy','Crime','Horror','Documentary','Biography','Drama','Romance','Sci-Fi','Thriller','Family','Fantasy','History','Mystery','Sport','Music']]
			targetTest = Test.gross

			regr = linear_model.LinearRegression()
			regr.fit(featureTrain, targetTrain)
			predictions = regr.predict(featuresTest)
		
			target = list(targetTest)

			#for i in range(len(target)):
				#print predictions[i],target[i]
			

			predictions = list(predictions)
			for i in range(len(target)):
				target[i] =  float(target[i])
			
			#print predictions
			#print target
			rmse =  math.sqrt(mse(predictions,target))
			print rmse
			mean_.append(rmse)
			#print rmse
			

			print (rmse/me) * 100
		
		rmse =  sum(mean_)/len(mean_)
		#print rmse
		#datacollected_gross =  datacollected[condition_five]
		
		#me =  np.mean(list(datacollected.gross))
		print (rmse/me) * 100
		#print min(gross)
		#print max(gross)
		#print me


if __name__=='__main__':
	main()