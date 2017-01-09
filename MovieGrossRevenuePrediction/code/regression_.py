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

def mape(est,real):
	e = est;
	r = real;

	rr = []
	ee = []

	for i in xrange(len(r)):
		rr.append(r[i])
		ee.append(e[i])

	rr = np.array(rr)
	ee = np.array(ee)

	err = sum(abs(rr - ee) / rr);
	err = err *100 / len(r);
	return err

def main():

	data = {}
	startyear = 2000
	endyear = 2015
	budget = []
	opening_weekend = []
	screens = []
	gross = []
	userreviews = []
	#metascore = []
	#imdb_rating = []
	count = 0
	while startyear <=endyear:
		inf= '../output_rotten/'+str(startyear)+'/Genre_inflation/Action_'+str(startyear)+'.json'
		with open(inf,'r') as jfin:
			data1 = json.load(jfin)

		for key,value in data1.iteritems():
			#if data1[key]['popularity'].find('</span') != -1:
				#print key,startyear
			if data1[key]['budget']!= 'empty' and data1[key]['OpeningWeekend'] != 'empty' and data1[key]['Screens'] != 'empty' and data1[key]['Gross'] != 'empty' and data1[key]['userreviews'] != 'empty':
				count = count + 1
				budget.append(long(data1[key]['budget']))
				opening_weekend.append(long(data1[key]['OpeningWeekend']))
				screens.append(long(data1[key]['Screens']))
				gross.append(long(data1[key]['Gross']))
				userreviews.append(long(data1[key]['userreviews']))
				#imdb_rating.append(float(data1[key]['imdb_rating']))
				#metascore.append(long(data1[key]['metascore']))


		startyear = startyear + 1


	budget = np.asarray(budget)
	opening_weekend = np.asarray(opening_weekend)
	screens = np.asarray(screens)
	gross = np.asarray(gross)
	userreviews = np.asarray(userreviews)
	#metascore = np.asarray(metascore)
	#imdb_rating = np.asarray(imdb_rating)
	datacollected = pd.DataFrame({'budget':budget.transpose(),'screens':screens.transpose(),'opening_weekend':opening_weekend.transpose(),'gross':gross.transpose(), 'userreviews':userreviews.transpose()})



	total_items = len(datacollected.index)

	#print datacollected
	
	kf = KFold(total_items, n_folds=10)
	mean_ = []
	for train_index, test_index in kf:
		
		Train,Test = datacollected.iloc[train_index],datacollected.iloc[test_index]
		featureTrain = Train[["opening_weekend"]]

		targetTrain = Train.gross
		featuresTest = Test[["opening_weekend"]]
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
		mean_.append(rmse)
		#print rmse
		

		#print (rmse/me) * 100
	
	rmse =  sum(mean_)/len(mean_)
	#print rmse
	#datacollected_gross =  datacollected[condition_five]
	gross_ = list(datacollected.gross)
	Gr = []
	for i in range(len(gross_)):
		if gross_[i] != 'empty':
			Gr.append(float(gross_[i]))

	me = np.mean(Gr)
	#me =  np.mean(list(datacollected.gross))
	print (rmse/me) * 100
	#print min(Gr)
	#print max(Gr)
	#print me
	print mape(predictions,target)

if __name__=='__main__':
	main()