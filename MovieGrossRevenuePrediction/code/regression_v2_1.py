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
import itertools
def subs(l):
    res = []
    for i in range(1, len(l) + 1):
        for combo in itertools.combinations(l, i):
            res.append(list(combo))
    return res


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
	powerset = subs([0,1,2,3,4,5,6,7,8,9,10])
	minimum = {'Action':1000,'Adventure':1000,'Animation':1000,'Comedy':1000,'Crime':1000,'Horror':1000,'Documentary':1000,'Biography':1000,'Drama':1000,'Romance':1000,'Sci-Fi':1000,'Thriller':1000,'Family':1000,'Fantasy':1000,'History':1000,'Mystery':1000,'Sport':1000,'Music':1000}

	combination = {'Action':list(),'Adventure':list(),'Animation':list(),'Comedy':list(),'Crime':list(),'Horror':list(),'Documentary':list(),'Biography':list(),'Drama':list(),'Romance':list(),'Sci-Fi':list(),'Thriller':list(),'Family':list(),'Fantasy':list(),'History':list(),'Mystery':list(),'Sport':list(),'Music':list()}

	features_Set = {0:'budget',1:'opening_weekend',2:'screens',3:'metascore',4:'popularity',5:'imdb_rating',6:'tomatoMeter',7:'tomatoRating',8:'userMeter',9:'userrating',10:'userreviews'}
	for subset in powerset:
		set_features = subset
		print subset
		feature_list = []
		for ii in set_features:
			feature_list.append(features_Set[ii])
		for genre in genre_:
			PATH = "../output_rotten/csv_data/"+str(genre)+"_all.csv"
			if not os.path.isfile(PATH):
				generate_csv(genre)


			datacollected = pd.read_csv(PATH)
			#print datacollected
			drop_list = []
			#Clean Data
			for index, row in datacollected.iterrows():
				for i in set_features:
					if i == 3:
						if row['metascore'] == 'N/A' or math.isnan(row['metascore']):
							drop_list.append(index)
							continue
					if i == 9:
						if row['userrating'] == 'N':
							drop_list.append(index)
							continue
					if row[features_Set[i]] == 'empty' or row['gross'] == 'empty':
						drop_list.append(index)
				
			
			
			datacollected = datacollected.drop(datacollected.index[drop_list])
			
			total_items = len(datacollected.index)
			if total_items < 10:
				continue
			#print datacollected
			
			kf = KFold(total_items, n_folds=10)
			mean_ = []
			mape_ = []
			for train_index, test_index in kf:
				
				Train,Test = datacollected.iloc[train_index],datacollected.iloc[test_index]

				featureTrain = Train[feature_list]

				targetTrain = Train.gross
				featuresTest = Test[feature_list]
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
				Mape = mape(predictions,target)
				if Mape < 500:
					mape_.append(Mape)
					#print Mape
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
			#print genre,(rmse/me) * 100
			#print min(gross)
			#print max(gross)
			#print me
			#print genre,np.mean(mape_)
			if (minimum[genre] > np.mean(mape_)):
				minimum[genre] = np.mean(mape_)
				combination[genre] = subset
	print minimum
	print combination

if __name__=='__main__':
	main()