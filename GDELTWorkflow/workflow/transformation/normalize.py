from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

import pandas as pd
import numpy as np
from sklearn import preprocessing

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import threadconfig


df = pd.read_csv("/home/amanda/FYP/testcsv/RFout.csv")
colsToNormalize = userScript.userDefinedNormalizeColumns


'''
array = dataframe.values

scaler = Normalizer().fit(array)
normalized = scaler.transform(array)

# summarize transformed data
numpy.set_printoptions(precision=3)
'''
@python_app
def normalize(startColIndex, endColIndex, dFrame, ccolsToNormalize):

	df = pd.DataFrame()
	df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]

	colNames = list(df)
	print(colNames)
	# Normalize The Column
	# Create x, where x the 'scores' column's values as floats
	x = df[ccolsToNormalize].values.astype(float)
	print(x)

	# Create a minimum and maximum processor object
	min_max_scaler = preprocessing.MinMaxScaler()
	# Create an object to transform the data to fit minmax processor
	x_scaled = min_max_scaler.fit_transform(x)

	# Run the normalizer on the dataframe
	df_normalized = pd.DataFrame(x_scaled)
	j = 0
	for i in ccolsToNormalize:
		
		df[i] = df_normalized[j]
		j=j+1
	return df


print(normalize(0,7,df,['AvgTone', 'QuadClass']).result())
#this returns the column(s) that was normalized. 
#drop the previous column and concat at the end.
#parallelize the number of cols in the user script instruction - change for mode, normalize, encode



