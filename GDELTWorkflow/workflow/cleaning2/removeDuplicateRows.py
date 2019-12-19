from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

import pandas as pd
import numpy as np
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript2
#import threadconfig

df = pd.read_csv(userScript2.outputLocation + "dropUniqueColumns.csv")
outputDataset = userScript2.outputLocation + "removeDuplicateRows.csv"

@python_app
def removeDuplicateRows(startRowIndex, endRowIndex, dFrame):

	df = pd.DataFrame()
	df = dFrame.iloc[np.r_[startRowIndex : endRowIndex] , : ]
	dfDroppedDuplicates = df.drop_duplicates()
	dfDroppedDuplicates.reset_index(inplace=True)
	
	return dfDroppedDuplicates


#read csv with defined missing values
numOfRows = df.shape[0]
#print(numOfRows)


dfNew = pd.DataFrame()
maxThreads = 4

results = []

#not parallel --> relatively small number of rows here
if numOfRows <= maxThreads:
	df1 = removeDuplicateRows(0, numOfRows, df)
	results.append(df1)

#parallel
elif numOfRows > maxThreads:
	#print("test2")
	if (numOfRows % maxThreads == 0):
		eachThreadRows = numOfRows / maxThreads 
		for i in range (maxThreads):
			df1 = removeDuplicateRows(i,(i+eachThreadRows),df)
			results.append(df1)
			#dfNew = pd.concat([dfNew, df1] , axis=0)
		
	else:
		eachThreadRows = numOfRows // (maxThreads-1)
		for i in range (0,(maxThreads-1)*eachThreadRows, eachThreadRows):
			#print ("i", i)
			#print("i+eachThreadRows", (i+eachThreadRows))
			df1 = removeDuplicateRows(i, (i+eachThreadRows), df)
			results.append(df1)
			#dfNew = pd.concat([dfNew, df1], axis=0)

		print("last thread",(eachThreadRows * (maxThreads-1))	)
		df2 = removeDuplicateRows((eachThreadRows * (maxThreads-1)), numOfRows, df)
		results.append(df2)
	
		#dfNew = pd.concat([dfNew, df2] , axis=0)


# wait for all apps to complete
#[r.result() for r in results]


newlist = []	
for i in results:
	newlist.append(i.result())

for i in newlist:
	
	dfNew = pd.concat([dfNew, i], axis=0)


#dfNew = newlist[0]
#print(dfNew)

dfNew.drop("index",inplace=True,axis=1)
#print(dfNew)

dfNew.to_csv (outputDataset, index = False, header=True)
#print(removeDuplicateRows(50,100,df).result())

print("Module Completed: Remove Duplicate Rows")
