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
import userScript

currentModule = "dropColumnsCriteria"
df = pd.DataFrame()
for i in range(len(userScript.orderOfModules)):
	#print(userScript.orderOfModules[i])
	if currentModule == userScript.orderOfModules[i]:
		if i == 0:
			df = pd.read_csv(userScript.inputDataset)
			break
		else:
			previousModule = userScript.orderOfModules[i-1]
			df = pd.read_csv(userScript.outputLocation + previousModule + ".csv")
			break

outputDataset = userScript.outputLocation + currentModule + ".csv"
#user defined percentage of maximum of allowed missing values
maxPercentageOfMissingValues= userScript.userDefinedColPercentage
dropList = []

@python_app
def dropColumnsCriteria(startColIndex, endColIndex, dFrame, maxPercentage, dropList):

	import pandas as pd
	import numpy as np


	#function to count thr number of missing values in a given column
	def countMissingValues(colName, df):
	  dfCol = df[colName]
	  return dfCol.isnull().sum()

	df = pd.DataFrame()
	df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]

	colNames = list(df)
	noOfRows = df.shape[0]

#	dfMissingValueCriteriaDropped=df

	for col in df.columns:
	  noMissingValues = countMissingValues(col,df)

	  if ((noMissingValues/noOfRows)>(maxPercentage/100)):
	    #dfMissingValueCriteriaDropped = dfMissingValueCriteriaDropped.drop(i, axis=1)
	    dropList.append(col)

	#ret = dfMissingValueCriteriaDropped

	return dropList

numOfCols = df.shape[1]

lasThreadCols = 0

dfNew = pd.DataFrame()

maxThreads = 3
results = []

if numOfCols <= maxThreads:
	for i in range (numOfCols):
		dList1 = dropColumnsCriteria(i, i+1, df, maxPercentageOfMissingValues, dropList)
		results.append(dList1)

elif numOfCols > maxThreads:
	eachThreadCols = numOfCols // maxThreads
	if (numOfCols % maxThreads == 0):
		#print("test2")
		for i in range (0,(maxThreads)*eachThreadCols, eachThreadCols):
			dList1 = dropColumnsCriteria(i,(i+eachThreadCols),df,maxPercentageOfMissingValues, dropList)
			#dfNew = pd.concat(dfNew, df1)
			results.append(dList1)

	else:
		#print("test3")
		#for loop for the threads
		for i in range (0,(maxThreads*eachThreadCols), eachThreadCols):
			#print ("i", i)
			#print("i+eachThreadCols", (i+eachThreadCols))
			dList1 = dropColumnsCriteria(i,(i+eachThreadCols),df,maxPercentageOfMissingValues, dropList)
			#dfNew = pd.concat([dfNew, df1], axis=1)
			results.append(dList1)

		#non parallel
		dList2 = dropColumnsCriteria((eachThreadCols * maxThreads),numOfCols,df,maxPercentageOfMissingValues, dropList)
		results.append(dList2)
		#dfNew = pd.concat([dfNew, df2] , axis=1)


# wait for all apps to complete
[r.result() for r in results]

df.drop(dropList,inplace=True,axis=1)
df.to_csv (outputDataset, index = False, header=True)
print("Module Completed: Drop Columns based on User Defined Criteria")
