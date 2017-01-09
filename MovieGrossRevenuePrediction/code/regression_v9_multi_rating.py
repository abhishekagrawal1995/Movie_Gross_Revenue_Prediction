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
def generate_csv(genre,mean_std_l,mean_std_h):
	data = {}
	startyear = 2000
	endyear = 2013
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
	budget_l = []
	opening_weekend_l = []
	screens_l = []
	gross_l = []
	userreviews_l = []
	userrating_l =[]
	userMeter_l = []
	tomatoRating_l =[]
	
	tomatoMeter_l = []
	metascore_l = []
	imdb_rating_l = []
	popularity_l = []
	ttnumber_l = []
	count = 0
	while startyear <=endyear:
		inf= '../output_rotten/'+str(startyear)+'/Genre_inflation/'+str(genre)+'_'+str(startyear)+'.json'
		with open(inf,'r') as jfin:
			data1 = json.load(jfin)

		for key,value in data1.iteritems():
			#if data1[key]['popularity'].find('</span') != -1:
				#print key,startyear
			count = count + 1
			Screens  = data1[key]['Screens']
			rating = data1[key]['tomatoRating']

			#print rating
			if rating != 'empty':
				if float(rating) > 5.0:
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
				else:
					ttnumber_l.append(key)
					budget_l.append(data1[key]['budget'])
					opening_weekend_l.append(data1[key]['OpeningWeekend'])
					screens_l.append(data1[key]['Screens'])
					gross_l.append(data1[key]['Gross'])
					userreviews_l.append(data1[key]['userreviews'])

					userrating_l.append(data1[key]['userrating'])
					userMeter_l.append(data1[key]['userMeter'])
					tomatoRating_l.append(data1[key]['tomatoRating'])
					
					tomatoMeter_l.append(data1[key]['tomatoMeter'])
					popularity_l.append(data1[key]['popularity'])
					imdb_rating_l.append(data1[key]['imdb_rating'])
					metascore_l.append(data1[key]['metascore'])


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

	budget_l = np.asarray(budget_l)
	opening_weekend_l = np.asarray(opening_weekend_l)
	screens_l = np.asarray(screens_l)
	gross_l = np.asarray(gross_l)
	userreviews_l = np.asarray(userreviews_l)
	userrating_l = np.asarray(userrating_l)
	userMeter_l = np.asarray(userMeter_l)
	tomatoRating_l = np.asarray(tomatoRating_l)
	tomatoMeter_l = np.asarray(tomatoMeter_l)
	popularity_l = np.asarray(popularity_l)

	metascore_l = np.asarray(metascore_l)
	imdb_rating_l = np.asarray(imdb_rating_l)
	ttnumber_l = np.asarray(ttnumber_l)
	datacollected = pd.DataFrame({'ttnumber':ttnumber.transpose(),'budget':budget.transpose(),'Screens':screens.transpose(),'OpeningWeekend':opening_weekend.transpose(),'Gross':gross.transpose(),'userreviews':userreviews.transpose(),'userrating':userrating.transpose(),'userMeter':userMeter.transpose(),'tomatoRating':tomatoRating.transpose(),'tomatoMeter':tomatoMeter.transpose(),'popularity':popularity.transpose(),'imdb_rating':imdb_rating.transpose(),'metascore':metascore.transpose()})
	datacollected_l = pd.DataFrame({'ttnumber':ttnumber_l.transpose(),'budget':budget_l.transpose(),'Screens':screens_l.transpose(),'OpeningWeekend':opening_weekend_l.transpose(),'Gross':gross_l.transpose(),'userreviews':userreviews_l.transpose(),'userrating':userrating_l.transpose(),'userMeter':userMeter_l.transpose(),'tomatoRating':tomatoRating_l.transpose(),'tomatoMeter':tomatoMeter_l.transpose(),'popularity':popularity_l.transpose(),'imdb_rating':imdb_rating_l.transpose(),'metascore':metascore_l.transpose()})
	

	#print df
	drop_list = []
	drop_list_l = []
	
	#Clean Data
	for index, row in datacollected.iterrows():
		
		if row['budget'] == 'empty' or row['Gross'] == 'empty' or row['Screens'] == 'empty' or row['OpeningWeekend'] == 'empty' or row['popularity'] == 'empty' or row['tomatoMeter']=='empty' or row['tomatoRating'] == 'empty':
			drop_list.append(index)
	
	for index, row in datacollected_l.iterrows():
		
		if row['budget'] == 'empty' or row['Gross'] == 'empty' or row['Screens'] == 'empty' or row['OpeningWeekend'] == 'empty' or row['popularity'] == 'empty' or row['tomatoMeter']=='empty' or row['tomatoRating'] == 'empty':
			drop_list_l.append(index)

	datacollected = datacollected.drop(datacollected.index[drop_list])
	datacollected_l = datacollected_l.drop(datacollected_l.index[drop_list_l])
	df = datacollected
	df_l = datacollected_l
	df = df[df.budget == '0']
	df_l = df_l[df_l.budget == '0']

	feature_names = ["budget","imdb_rating","metascore","OpeningWeekend","popularity","Screens","tomatoMeter","tomatoRating","userMeter","userrating","userreviews"]
	

	for index,row in datacollected.iterrows():
		for feature in feature_names:
			x = row[feature]
			x = float(x)
			m = float(mean_std_h[feature]['mean'])
			mm = float(mean_std_h[feature]['std'])
	
			y = (float)(x - m)
		
			y = (float)(y/(mm))
			
			row[feature] = str(y)
		df.loc[-1] = row
		df.index = df.index + 1  # shifting index
 		df = df.sort() 


 	for index,row in datacollected_l.iterrows():
		for feature in feature_names:
			x = row[feature]
			x = float(x)
			m = float(mean_std_l[feature]['mean'])
			mm = float(mean_std_l[feature]['std'])
	
			y = (float)(x - m)
		
			y = (float)(y/(mm))
			
			row[feature] = str(y)
		df_l.loc[-1] = row
		df_l.index = df_l.index + 1  # shifting index
 		df_l = df_l.sort() 
	df.to_csv('../output_rotten/csv_data_00_14/'+str(genre)+'_all_high.csv',index = False)
	df_l.to_csv('../output_rotten/csv_data_00_14/'+str(genre)+'_all_low.csv',index = False)

def main():
	#genre = str(sys.argv[1])
	genre_ = ['Action','Adventure','Animation','Comedy','Crime','Horror','Documentary','Biography','Drama','Romance','Sci-Fi','Thriller','Family','Fantasy','History','Mystery','Sport','Music']
	combination = {'Action':list(),'Adventure':list(),'Animation':list(),'Comedy':list(),'Crime':list(),'Horror':list(),'Documentary':list(),'Biography':list(),'Drama':list(),'Romance':list(),'Sci-Fi':list(),'Thriller':list(),'Family':list(),'Fantasy':list(),'History':list(),'Mystery':list(),'Sport':list(),'Music':list()}

	combination = {'Mystery': [0, 1, 4, 10], 'Romance': [0, 1, 10], 'Sport': [0, 1, 3, 4, 6, 7], 'Sci-Fi': [1], 'Family': [0, 1, 4, 7, 10], 'Horror': [1, 10], 'Thriller': [0, 1], 'Crime': [0, 1], 'Drama': [0, 1, 4], 'Fantasy': [0, 1, 2, 4, 9], 'Animation': [0, 1], 'Music': [0, 1, 6, 10], 'Adventure': [0, 1], 'Action': [1, 4], 'Comedy': [0, 1], 'Documentary': [4, 7, 9, 10], 'Biography': [0, 1, 3, 4, 6, 7], 'History': [1, 4, 7]}
	features_Set = {0:'budget',1:'OpeningWeekend',2:'Screens',3:'metascore',4:'popularity',5:'imdb_rating',6:'tomatoMeter',7:'tomatoRating',8:'userMeter',9:'userrating',10:'userreviews',11:'Gross'}
	reverse_features_Set_csv = {'budget':0,'opening_weekend':1,'screens':2,'metascore':3,'popularity':4,'imdb_rating':5,'tomatoMeter':6,'tomatoRating':7,'userMeter':8,'userrating':9,'userreviews':10,'gross':11}
	features_Set_csv = {0:'budget',1:'opening_weekend',2:'screens',3:'metascore',4:'popularity',5:'imdb_rating',6:'tomatoMeter',7:'tomatoRating',8:'userMeter',9:'userrating',10:'userreviews',11:'gross'}
	#print len(genre_)
	
	testfilename = '../output_rotten/'+'/movies_merge_clean_inflation_2014_15'+'.json'
	meanfilename_l = '../output_rotten/'+'/mean_std_l'+'.json'
	meanfilename_h = '../output_rotten/'+'/mean_std_h'+'.json'
	with open(testfilename,'r') as jfin:
		keys = json.load(jfin)


	with open(meanfilename_l,'r') as jfin:
		mean_std_l = json.load(jfin)

	with open(meanfilename_h,'r') as jfin:
		mean_std_h = json.load(jfin)

	predict_gross = []
	real_gross = []
	iid_l = 1
	iid_h = 400

	genre_dict = {}

	counter = 0
	counter_high = 0
	flag = 0
	
	MAPE = []
	for genre in genre_:
		#PATH = "../output_rotten/csv_data_00_14/"+str(genre)+"_all.csv"
		generate_csv(genre,mean_std_l,mean_std_h)
			


	#print min_max_map_all

	for key, value in keys.iteritems():

		if iid_l == iid_h:
			break

		iid_l = iid_l + 1
		genre_list = []
		

		genre_1 = keys[key]['Genre']

		'''
		budget_ = keys[key]['budget']
		screens_ = keys[key]['Screens']
		opening_weekend_ = keys[key]['OpeningWeekend']
		'''
		gross_ = keys[key]['Gross']
		'''
		if budget_ == 'empty' or screens_ == 'empty' or opening_weekend_ == 'empty' or gross_ == 'empty' :
			continue
		'''
		if gross_ == 'empty' :
			continue


		

		genre_dict[key] = {}
		#genre_dict[key]['gross'] = 0


		

		for l in genre_1:
			if l in genre_:
				genre_list.append(l)


		if len(genre_list) == 0:
			continue

		for i in genre_list:
			genre_dict[key][i] = 0

		genre_value = []
		
		flag = 0
		for genre in genre_list:

			can_predict = 0
			Screens = keys[key]['Screens']
			rating = keys[key]['tomatoRating']
			if rating == 'empty':
				continue
			if float(rating) > 5.0:
				mean_std = mean_std_h
				PATH = "../output_rotten/csv_data_00_14/"+str(genre)+"_all_high.csv"
				if flag == 0:
					counter_high = counter_high + 1
					flag = 1
			else:
				continue
				mean_std = mean_std_l
				PATH = "../output_rotten/csv_data_00_14/"+str(genre)+"_all_low.csv"
			'''
			if not os.path.isfile(PATH):
				#print "hellp"
				map_minmax = generate_csv(genre)
				min_max_map_all[genre] = map_minmax

			'''
			datacollected = pd.read_csv(PATH)
			#print datacollected
			drop_list = []

			
			#Clean Data
			combination_genre = combination[genre]
			best_combination = []
			

			for i in combination_genre:
				best_combination.append(features_Set[i])

			


			for best in best_combination:
				if keys[key][best] == 'empty' or keys[key][best] == 'N/A' or keys[key][best] == 'N':
					can_predict =  1
					break

			if can_predict == 1:
				continue


			for index,row in datacollected.iterrows():
				for ii in best_combination:
					if row[ii] == 'empty' or row[ii] == 'N/A' or row[ii] == 'N':
						drop_list.append(index)
						break

				

			'''
			for index, row in datacollected.iterrows():
				if row['ttnumber'] == key:
					drop_list.append(index)
				if row['budget'] == 'empty' or row['gross'] == 'empty' or row['screens'] == 'empty' or row['opening_weekend'] == 'empty':
					#print index
					drop_list.append(index)
			'''
			


			datacollected = datacollected.drop(datacollected.index[drop_list])
				
			featureTrain = datacollected[best_combination]
			#print featureTrain
			targetTrain = datacollected.Gross
			
			regr = linear_model.LinearRegression()
			#print len(featureTrain.index)
			if len(featureTrain.index) == 0:
				continue
			regr.fit(featureTrain, targetTrain)

			input_list = list()
			for best in best_combination:
				

				x = keys[key][best]
				x = float(x)
				#print genre
				m = float(mean_std[best]['mean'])
				mm = float(mean_std[best]['std'])
				
				
				y = (float)(x - m)
		
				y = (float)(y/(mm))
				
				
				input_list.append(float(y))
				'''
				input_list.append()
				input_list.append(float(keys[key][best]))
				'''
			'''
			input_list.append(long(budget_))
			input_list.append(long(screens_))
			input_list.append(long(opening_weekend_))
			'''

			predictions = regr.predict([input_list])
			#print predictions
			
			
			
			genre_value.append(predictions[0])
			genre_dict[key][genre] = predictions[0]


			#print genre,predictions[0]
		#genre_dict[key]['gross'] = gross_
		#print gross_
		#print key
		#print value
		if len(genre_value) == 0:
			continue
		
		#Add Gross
		gross_ = keys[key]['Gross']
		
		r = []
		t = []
		r.append(float(gross_))

		genre_mean = sum(genre_value)/len(genre_value)
		'''
		if mean_std == mean_std_l:
			genre_mean = (max(genre_value)+min(genre_value))/2
		else:
			genre_mean = (min(genre_value)+max(genre_value))/2
		'''
		t.append(float(genre_mean))
		Mape = mape(t,r)
		if Mape < 200:
			predict_gross.append(genre_mean)
			real_gross.append(float(gross_))
		
		#print Mape
		if Mape > 200 :
			counter = counter + 1
		
		


	print predict_gross
	print real_gross
	Mape = mape(predict_gross,real_gross)
	print Mape
	#print counter
	#print counter_high
	#print sum(MAPE)/len(MAPE)
	
			
			

if __name__=='__main__':
	main()