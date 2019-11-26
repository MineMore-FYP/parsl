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
import dataType


df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")
colsToNormalize = userScript.userDefinedNormalizeColumns

for i in colsToNormalize:
	if dataType.dataType(i, df) == "str":
		print("Cannot normalize string column: ", i)
		colsToNormalize.remove(i)
	
print(colsToNormalize)

@python_app
def normalize(startColIndex, endColIndex, dFrame, normalizeCols):
	import pandas as pd
	import numpy as np
	from sklearn import preprocessing

	df = pd.DataFrame()
	df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]

	dfColNames = list(df)
	normalizeCols = list(set(dfColNames).intersection(normalizeCols))
	print(normalizeCols)

	if len(normalizeCols)!=0:


		# Normalize The Column
		# Create x, where x the 'scores' column's values as floats
		x = df[normalizeCols].values.astype(float)
		print(x)

		# Create a minimum and maximum processor object
		min_max_scaler = preprocessing.MinMaxScaler()
		# Create an object to transform the data to fit minmax processor
		x_scaled = min_max_scaler.fit_transform(x)

		# Run the normalizer on the dataframe
		df_normalized = pd.DataFrame(x_scaled)
		j = 0
		#replace the normalized column in the original df
		for i in normalizeCols:
			df[i] = df_normalized[j]
			j=j+1
	return df


#print(normalize(0,3,df,['AvgTone', 'QuadClass']).result())
#this returns the column(s) that was normalized. 
#drop the previous column and concat at the end.
#parallelize the number of cols in the user script instruction - change for mode, normalize, encode


maxThreads = threadconfig.maxThreads

numOfCols = df.shape[1]
print(numOfCols)

lasThreadCols = 0
dfNew = pd.DataFrame()

results = []

#one col per thread
if numOfCols <= maxThreads:
	for i in range (numOfCols):
		df1 = normalize(i, i+1, df, colsToNormalize)
		results.append(df1)		
		#print (df1)
		#dfNew = pd.concat([dfNew, df1] , axis=1)


elif numOfCols > maxThreads:
	print("test2")
	if (numOfCols % maxThreads == 0):
		eachThreadCols = numOfCols / maxThreads 
		for i in range (maxThreads):
			df1 = normalize(i,(i+eachThreadCols),df,colsToNormalize)
			#dfNew = pd.concat([dfNew, df1] , axis=1)
			results.append(df1)
		
	else:
		eachThreadCols = numOfCols // (maxThreads-1)
		lasThreadCols = numOfCols % (maxThreads-1)
		for i in range (0,(maxThreads-1)*eachThreadCols, eachThreadCols):
			print ("i", i)
			print("i+eachThreadCols", (i+eachThreadCols))
			df1 = normalize(i,(i+eachThreadCols),df,colsToNormalize)
			#dfNew = pd.concat([dfNew, df1], axis=1)
			results.append(df1)

		print("last thread",(eachThreadCols * (maxThreads-1))	)
		df2 = normalize((eachThreadCols * (maxThreads-1)),numOfCols,df,colsToNormalize)
		results.append(df1)
		#dfNew = pd.concat([dfNew, df2] , axis=1)


newlist = []	
for i in results:
	newlist.append(i.result())

for i in newlist:
	
	dfNew = pd.concat([dfNew, i], axis=1)



print(dfNew)
dfNew.to_csv ("/home/amanda/FYP/testcsv/normalize.csv", index = False, header=True)


