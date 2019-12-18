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


currentModule = "removeDuplicateRows"
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

@python_app
def removeDuplicateRows(startRowIndex, endRowIndex, dFrame):

	df = pd.DataFrame()
	df = dFrame.iloc[np.r_[startRowIndex : endRowIndex] , : ]
	dfDroppedDuplicates = df.drop_duplicates()
	dfDroppedDuplicates.reset_index(inplace=True)

	return dfDroppedDuplicates

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
	eachThreadRows = numOfRows // maxThreads
	for i in range (0,(maxThreads*eachThreadRows), eachThreadRows):
		df1 = removeDuplicateRows(i,(i+eachThreadRows),df)
		results.append(df1)
	if (numOfRows % maxThreads != 0):
		df2 = removeDuplicateRows((eachThreadRows * (maxThreads-1)), numOfRows, df)
		results.append(df2)

# wait for all apps to complete
[r.result() for r in results]


newlist = []
for i in results:
	newlist.append(i.result())

#concat all the dfs into one row wise
for i in newlist:
	dfNew = pd.concat([dfNew, i], axis=0)


#dfNew = newlist[0]
#print(dfNew)

dfNew.drop("index",inplace=True,axis=1)
#print(dfNew)

dfNew.to_csv (outputDataset, index = False, header=True)
print("Module Completed: Remove Duplicate Rows")
