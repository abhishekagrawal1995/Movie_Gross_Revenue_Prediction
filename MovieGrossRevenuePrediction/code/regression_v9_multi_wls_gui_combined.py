
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
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import KFold
import sys
import os
from sklearn.svm import SVR

def sort(dist_list,ind_list):
	for i in range(0,len(dist_list)-1):
		mini_index = i
		for j in range(i+1,len(dist_list)):
			if dist_list[j] < dist_list[mini_index]:
				mini_index = j

		if mini_index != i :
			flag = dist_list[mini_index]
			dist_list[mini_index] = dist_list[i]
			dist_list[i] = flag
			flag_index = ind_list[mini_index]
			ind_list[mini_index] = ind_list[i]
			ind_list[i] = flag_index

	neighbours = min(50,len(dist_list)) 
	return [ind_list,neighbours]


def findneighbour(features,target,inputs,best_combination):
	
	distances = {}
	for index,row in features.iterrows():
		distances[index] = 0

	for i in range(len(inputs)):
		for index,row in features.iterrows():
			x = row[best_combination[i]]
			x = float(x)
			y = (x-inputs[i])*(x-inputs[i])
			distances[index] = distances[index] + float(y)


	for index,row in features.iterrows():
		distances[index] = float(math.sqrt(float(distances[index])))

	dist_list = []
	ind_list = []
	for key in distances:
		ind_list.append(key)
		dist_list.append(distances[key])

	
	[ind_list,neighbours] = sort(dist_list,ind_list)
	
	neigh_ind = []
	for i in range(0,neighbours):
		neigh_ind.append(ind_list[i])

	drop_list = []
	for index,row in features.iterrows():
		if index not in neigh_ind:
			drop_list.append(index)

	df = features.drop(features.index[drop_list])
	df_target = target.drop(target.index[drop_list])
	return [df,df_target]


def lwr_predict(x,y,datapoint):
    c = 1.0
    weights = []

    for i in range(len(x)):
    	datapoint = float(datapoint)

        #xx = float((float(x[i])-datapoint)*(float(x[i])-datapoint))
        #xx = 1.0/xx
        xx = float((float(x[i])-datapoint))
        xx =  abs(xx) * (0.20)
        yy = xx
        #xx  =  xx
        #yy = math.exp(xx)
        #yy = math.exp((xx)/(-2.0* c**2))
        weights.append(yy)

    summ = 0
    for i in range(len(weights)):
        summ = summ + x[i]*x[i]*weights[i]

    summ = 1.0/summ 


    summ1 = 0
    for i in range(len(weights)):
        summ1 = summ1 + x[i]*y[i]*weights[i]

    beta = summ*summ1
    return beta

def localwreg(features,target,inputs,best_combination):

	[features,target] = findneighbour(features,target,inputs,best_combination)
	
	'''
	regr = linear_model.LinearRegression()
	regr.fit(features, target)
	predictions = regr.predict([inputs])
	return predictions[0]
	'''

	regr_1 = DecisionTreeRegressor(max_depth=7)
	regr_1.fit(features, target)
	y_1 = regr_1.predict([inputs])
	return y_1[0]
	




	'''
	gross_ = list(target)
	betas = []
	for i in range(len(inputs)):
		datapoint = float(inputs[i])
		feature = list(features[best_combination[i]])
		#print feature
		betas.append(lwr_predict(feature,gross_,datapoint))

	result  = 0
	for i in range(len(betas)):
		result = result + betas[i]*inputs[i]

	return result
	'''


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
def generate_csv_rating(genre,mean_std_l,mean_std_h):
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
	df.to_csv('../output_rotten/csv_data_00_14/'+str(genre)+'_all_high_rating.csv',index = False)
	df_l.to_csv('../output_rotten/csv_data_00_14/'+str(genre)+'_all_low_rating.csv',index = False)
def generate_csv_screens(genre,mean_std):
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
		inf= '/home/geekdon/Desktop/MovieData/output_rotten/'+str(startyear)+'/Genre_inflation/'+str(genre)+'_'+str(startyear)+'.json'
		with open(inf,'r') as jfin:
			data1 = json.load(jfin)

		for key,value in data1.iteritems():
			#if data1[key]['popularity'].find('</span') != -1:
				#print key,startyear
			count = count + 1
			Screens  = data1[key]['Screens']
			#rating = data1[key]['tomatoRating']

			#print rating
			if Screens != 'empty':
				if float(Screens) > mean_std['Screens']['mean']:
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
			m = float(mean_std[feature]['mean'])
			mm = float(mean_std[feature]['std'])
	
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
			m = float(mean_std[feature]['mean'])
			mm = float(mean_std[feature]['std'])
	
			y = (float)(x - m)
		
			y = (float)(y/(mm))
			
			row[feature] = str(y)
		df_l.loc[-1] = row
		df_l.index = df_l.index + 1  # shifting index
 		df_l = df_l.sort() 
	df.to_csv('/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/'+str(genre)+'_all_high_screens.csv',index = False)
	df_l.to_csv('/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/'+str(genre)+'_all_low_screens.csv',index = False)

def main():
	
	genre_list_java = str(sys.argv[1])
	input_list_java = str(sys.argv[2])


	genre_ = ['Action','Adventure','Animation','Comedy','Crime','Horror','Documentary','Biography','Drama','Romance','Sci-Fi','Thriller','Family','Fantasy','History','Mystery','Sport','Music']
	combination = {'Action':list(),'Adventure':list(),'Animation':list(),'Comedy':list(),'Crime':list(),'Horror':list(),'Documentary':list(),'Biography':list(),'Drama':list(),'Romance':list(),'Sci-Fi':list(),'Thriller':list(),'Family':list(),'Fantasy':list(),'History':list(),'Mystery':list(),'Sport':list(),'Music':list()}

	combination = {'Mystery': [0, 1, 4, 10], 'Romance': [0, 1, 10], 'Sport': [0, 1, 3, 4, 6, 7], 'Sci-Fi': [1], 'Family': [0, 1, 4, 7, 10], 'Horror': [1, 10], 'Thriller': [0, 1], 'Crime': [0, 1], 'Drama': [0, 1, 4], 'Fantasy': [0, 1, 2, 4, 9], 'Animation': [0, 1], 'Music': [0, 1, 6, 10], 'Adventure': [0, 1], 'Action': [1, 4], 'Comedy': [0, 1], 'Documentary': [4, 7, 9, 10], 'Biography': [0, 1, 3, 4, 6, 7], 'History': [1, 4, 7]}
	features_Set = {0:'budget',1:'OpeningWeekend',2:'Screens',3:'metascore',4:'popularity',5:'imdb_rating',6:'tomatoMeter',7:'tomatoRating',8:'userMeter',9:'userrating',10:'userreviews',11:'Gross'}
	reverse_features_Set = {'budget':0,'OpeningWeekend':1,'Screens':2,'metascore':3,'popularity':4,'imdb_rating':5,'tomatoMeter':6,'tomatoRating':7,'userMeter':8,'userrating':9,'userreviews':10,'Gross':11}

	reverse_features_Set_csv = {'budget':0,'opening_weekend':1,'screens':2,'metascore':3,'popularity':4,'imdb_rating':5,'tomatoMeter':6,'tomatoRating':7,'userMeter':8,'userrating':9,'userreviews':10,'gross':11}
	features_Set_csv = {0:'budget',1:'opening_weekend',2:'screens',3:'metascore',4:'popularity',5:'imdb_rating',6:'tomatoMeter',7:'tomatoRating',8:'userMeter',9:'userrating',10:'userreviews',11:'gross'}
	#print len(genre_)
	
	meanfilename_l = '/home/geekdon/Desktop/MovieData/output_rotten/'+'/mean_std_l'+'.json'
	meanfilename_h = '/home/geekdon/Desktop/MovieData/output_rotten/'+'/mean_std_h'+'.json'
	meanfilename = '/home/geekdon/Desktop/MovieData/output_rotten/'+'/mean_std'+'.json'
	
	with open(meanfilename,'r') as jfin:
		mean_std = json.load(jfin)
	
	with open(meanfilename_l,'r') as jfin:
		mean_std_l = json.load(jfin)

	with open(meanfilename_h,'r') as jfin:
		mean_std_h = json.load(jfin)
	

	predict_gross = []
	real_gross = []
	
	genre_dict = {}

	counter = 0
	counter_high = 0
	flag = 0
	
	MAPE = []
	for genre in genre_:
		#PATH = "../output_rotten/csv_data_00_14/"+str(genre)+"_all.csv"
		PATH = '/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/'+str(genre)+'_all_high_screens.csv'
		PATH1 = '/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/'+str(genre)+'_all_low_screens.csv'
		PATH2= '/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/'+str(genre)+'_all_low_rating.csv'
		PATH3 = '/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/'+str(genre)+'_all_high_rating.csv'
		if not os.path.isfile(PATH) and not os.path.isfile(PATH1) and not os.path.isfile(PATH2) and not os.path.isfile(PATH3):
			generate_csv_rating(genre,mean_std_l,mean_std_h)
			generate_csv_screens(genre,mean_std)
			


	genre_list = genre_list_java.split(',')
	input_ = input_list_java.split(',')

	genre_value = []
	
	flag = 0
	for genre in genre_list:

		can_predict = 0
		Screens = float(input_[2])
		#Screens = keys[key]['Screens']
		#rating = keys[key]['tomatoRating']
		rating = float(input_[7])
		if Screens == 'empty' or rating == 'empty':
			continue
		if float(Screens) > mean_std['Screens']['mean']:
			#print "Heyy"
			PATH = "/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/"+str(genre)+"_all_high_screens.csv"
			if flag == 0:
				counter_high = counter_high + 1
				flag = 1
		else:
			if float(rating) > 5.0:
				mean_std = mean_std_h
				PATH = "/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/"+str(genre)+"_all_high_rating.csv"
			else:
				mean_std = mean_std_l
				PATH = "/home/geekdon/Desktop/MovieData/output_rotten/csv_data_00_14/"+str(genre)+"_all_low_rating.csv"
			
		
		datacollected = pd.read_csv(PATH)
		#print datacollected
		drop_list = []

		
		#Clean Data
		combination_genre = combination[genre]
		best_combination = []
		

		for i in combination_genre:
			best_combination.append(features_Set[i])

		
		if can_predict == 1:
			continue


		for index,row in datacollected.iterrows():
			for ii in best_combination:
				if row[ii] == 'empty' or row[ii] == 'N/A' or row[ii] == 'N':
					drop_list.append(index)
					break

			
		datacollected = datacollected.drop(datacollected.index[drop_list])
			


		featureTrain = datacollected[best_combination]
		#print featureTrain
		targetTrain = datacollected.Gross
		
		regr = linear_model.LinearRegression()
		#print len(featureTrain.index)
		if len(featureTrain.index) == 0:
			continue


		input_list = list()
		for best in best_combination:
			

			x = input_[reverse_features_Set[best]]

			x = float(x)
			#print genre
			m = float(mean_std[best]['mean'])
			mm = float(mean_std[best]['std'])
			
			
			y = (float)(x - m)
	
			y = (float)(y/(mm))
			
			
			input_list.append(float(y))
			

		
		#regr.fit(featureTrain, targetTrain)
		#predictions = regr.predict([input_list])
		#print predictions
		predictions = localwreg(featureTrain,targetTrain,input_list,best_combination)
		genre_value.append(predictions)
		#genre_dict[key][genre] = predictions
		
		
	if len(genre_value) == 0:
		return 
	
	genre_mean = sum(genre_value)/len(genre_value)
	
	
	print genre_mean
	
			
			

if __name__=='__main__':
	main()