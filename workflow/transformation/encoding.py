#encoding
import pandas as pd
import numpy as np
import sys

import parsl
from parsl import load, python_app

# Import LabelEncoder
from sklearn import preprocessing
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
#import threadconfig

df = pd.read_csv(userScript.outputLocation + "splitIntoRows.csv")
outputDataset = userScript.outputLocation + "encoding.csv"

encodeCols = userScript.userDefinedEncodeColumns

@python_app
def encode(startColIndex, endColIndex, dFrame, encodeCols):
	import pandas as pd
	import numpy as np
	from sklearn import preprocessing

	df = pd.DataFrame()
	df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]

	dfColNames = list(df)
	encodeCols = list(set(dfColNames).intersection(encodeCols))
	#print(encodeCols)

	if len(encodeCols) != 0:
		x = df[encodeCols].astype(str)
		#creating labelEncoder
		le = preprocessing.LabelEncoder()
		# Converting string labels into numbers.
		encodedData=le.fit_transform(x)


		df_encoded = pd.DataFrame(encodedData)
		j = 0
		#replace the encoded column in the original df
		for i in encodeCols:
			df[i] = df_encoded[j]
			j=j+1
		
	return df

#print(encode(0,7, df, encodeCols).result())

maxThreads = 4

numOfCols = df.shape[1]
#print(numOfCols)

lasThreadCols = 0
dfNew = pd.DataFrame()

results = []

#one col per thread
if numOfCols <= maxThreads:
	for i in range (numOfCols):
		df1 = encode(i, i+1, df, encodeCols)
		results.append(df1)		
		#print (df1)
		#dfNew = pd.concat([dfNew, df1] , axis=1)

elif numOfCols > maxThreads:
	#print("test2")
	if (numOfCols % maxThreads == 0):
		eachThreadCols = numOfCols / maxThreads 
		for i in range (maxThreads):
			df1 = encode(i,(i+eachThreadCols),df,encodeCols)
			#dfNew = pd.concat([dfNew, df1] , axis=1)
			results.append(df1)
		
	else:
		eachThreadCols = numOfCols // (maxThreads-1)
		lasThreadCols = numOfCols % (maxThreads-1)
		for i in range (0,(maxThreads-1)*eachThreadCols, eachThreadCols):
			#print ("i", i)
			#print("i+eachThreadCols", (i+eachThreadCols))
			df1 = encode(i,(i+eachThreadCols),df,encodeCols)
			#dfNew = pd.concat([dfNew, df1], axis=1)
			results.append(df1)

		#print("last thread",(eachThreadCols * (maxThreads-1))	)
		df2 = encode((eachThreadCols * (maxThreads-1)),numOfCols,df,encodeCols)
		results.append(df1)
		#dfNew = pd.concat([dfNew, df2] , axis=1)

newlist = []	
for i in results:
	newlist.append(i.result())

for i in newlist:
	dfNew = pd.concat([dfNew, i], axis=1)

#print(dfNew)
dfNew.to_csv ("/home/amanda/FYP/testcsv/encode.csv", index = False, header=True)


