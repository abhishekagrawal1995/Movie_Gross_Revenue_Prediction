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

def generate_csv(genre):
	data = {}
	startyear = 2000
	endyear = 2015
	budget = []
	opening_weekend = []
	screens = []
	gross = []
	userreviews = []
	userrating =[]
	userMeter = []
	tomatoRating =[]
	tomatoMeter = []
	metascore = []
	imdb_rating = []
	popularity = []
	ttnumber = []
	count = 0
	while startyear <=endyear:
		inf= '../output_rotten/'+str(startyear)+'/Genre_inflation/'+str(genre)+'_'+str(startyear)+'.json'
		with open(inf,'r') as jfin:
			data1 = json.load(jfin)

		for key,value in data1.iteritems():
			#if data1[key]['popularity'].find('</span') != -1:
				#print key,startyear
			count = count + 1
			ttnumber.append(key)
			budget.append(data1[key]['budget'])
			opening_weekend.append(data1[key]['OpeningWeekend'])
			screens.append(data1[key]['Screens'])
			gross.append(data1[key]['Gross'])
			userreviews.append(data1[key]['userreviews'])

			userrating.append(data1[key]['userrating'])
			userMeter.append(data1[key]['userMeter'])
			tomatoRating.append(data1[key]['tomatoRating'])
			tomatoMeter.append(data1[key]['tomatoMeter'])
			popularity.append(data1[key]['popularity'])
			imdb_rating.append(data1[key]['imdb_rating'])
			metascore.append(data1[key]['metascore'])


		startyear = startyear + 1


	budget = np.asarray(budget)
	opening_weekend = np.asarray(opening_weekend)
	screens = np.asarray(screens)
	gross = np.asarray(gross)
	userreviews = np.asarray(userreviews)
	userrating = np.asarray(userrating)
	userMeter = np.asarray(userMeter)
	tomatoRating = np.asarray(tomatoRating)
	tomatoMeter = np.asarray(tomatoMeter)
	popularity = np.asarray(popularity)

	metascore = np.asarray(metascore)
	imdb_rating = np.asarray(imdb_rating)
	ttnumber = np.asarray(ttnumber)
	datacollected = pd.DataFrame({'ttnumber':ttnumber.transpose(),'budget':budget.transpose(),'screens':screens.transpose(),'opening_weekend':opening_weekend.transpose(),'gross':gross.transpose(),'userreviews':userreviews.transpose(),'userrating':userrating.transpose(),'userMeter':userMeter.transpose(),'tomatoRating':tomatoRating.transpose(),'tomatoMeter':tomatoMeter.transpose(),'popularity':popularity.transpose(),'imdb_rating':imdb_rating.transpose(),'metascore':metascore.transpose()})
	datacollected.to_csv('../output_rotten/csv_data/'+str(genre)+'_all.csv',index = False)

def main():
	#genre = str(sys.argv[1])
	genre_ = ['Action','Adventure','Animation','Comedy','Crime','Horror','Documentary','Biography','Drama','Romance','Sci-Fi','Thriller','Family','Fantasy','History','Mystery','Sport','Music']
	
	outfilename = '../output_rotten/'+'/movies_merge_clean_inflation_all'+'.json'
	
	with open(outfilename,'r') as jfin:
		keys = json.load(jfin)

	predict_gross = []
	real_gross = []
	iid_l = 1
	iid_h = 500

	for key, value in keys.iteritems():

		if iid_l == iid_h:
			break

		iid_l = iid_l + 1
		genre_list = []
		genre_1 = keys[key]['Genre']

		budget_ = keys[key]['budget']
		screens_ = keys[key]['Screens']
		opening_weekend_ = keys[key]['OpeningWeekend']
		gross_ = keys[key]['Gross']
		if budget_ == 'empty' or screens_ == 'empty' or opening_weekend_ == 'empty' or gross_ == 'empty' :
			continue


		real_gross.append(float(gross_))

		for l in genre_1:
			if l in genre_:
				genre_list.append(l)


		genre_value = []
		for genre in genre_list:
			PATH = "../output_rotten/csv_data/"+str(genre)+"_all.csv"
			if not os.path.isfile(PATH):
				generate_csv(genre)


			datacollected = pd.read_csv(PATH)
			#print datacollected
			drop_list = []
			#Clean Data
			for index, row in datacollected.iterrows():
				if row['ttnumber'] == key:
					drop_list.append(index)
				if row['budget'] == 'empty' or row['gross'] == 'empty' or row['screens'] == 'empty' or row['opening_weekend'] == 'empty':
					#print index
					drop_list.append(index)
			
			
			datacollected = datacollected.drop(datacollected.index[drop_list])
				
			featureTrain = datacollected[["budget","screens","opening_weekend"]]

			targetTrain = datacollected.gross
			
			regr = linear_model.LinearRegression()
			regr.fit(featureTrain, targetTrain)
			input_list = list()
			input_list.append(long(budget_))
			input_list.append(long(screens_))
			input_list.append(long(opening_weekend_))
			
			predictions = regr.predict([input_list])
			#print predictions
			genre_value.append(predictions[0])
			#print genre,predictions[0]
		#print gross_
		genre_mean = sum(genre_value)/len(genre_value)
		predict_gross.append(genre_mean)

	#print predict_gross
	#print real_gross
	print mape(predict_gross,real_gross)
	msse =  mse(predict_gross,real_gross)
	rmse = math.sqrt(msse)
	me =  np.mean(real_gross)
	#print me
	#print (rmse/me) * 100

			
			
			

			
			
			


if __name__=='__main__':
	main()