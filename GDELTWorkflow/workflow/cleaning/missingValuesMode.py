from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

import pandas as pd
import numpy as np
import statistics
from statistics import mode, StatisticsError

import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import userScript
import dataType
pd.options.mode.chained_assignment = None  # default='warn'

currentModule = "missingValuesMode"
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
colsToMode = userScript.modeColumns

@python_app
def missingValuesMode(startColIndex, endColIndex, dFrame, colsMode):

    df = pd.DataFrame()
    df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]
    numOfRows = df.shape[0]

    #drop unique columns
    for col in df.columns:
        if len(df[col].unique()) == numOfRows:
            df.drop(col,inplace=True,axis=1)

    if(colsMode == "all"):
        #Mode of all columns
        colNames = list(df)
    else:
        #Mode of user defined columns
        colNames = colsMode

    df2 = df
    df1 = pd.DataFrame()

    for col in colNames:
        try:
            df1 = df[col].dropna()
            modeOfCol = statistics.mode(df1)
            df2[col].fillna(modeOfCol, inplace = True)
        except StatisticsError:
            print(col)
            print ("No unique mode found")



    ret  = df2
    return ret

maxThreads = 4
numOfCols = df.shape[1]
#print(numOfCols)
dfNew = pd.DataFrame()
results = []

#one col per thread
if numOfCols <= maxThreads:
	for i in range (numOfCols):
		print("test1")
		df1 = missingValuesMode(i, i+1, df, colsToMode)
		results.append(df1)

elif numOfCols > maxThreads:
	#print("test2")
	eachThreadCols = numOfCols // maxThreads
	for i in range (0,(maxThreads)*eachThreadCols, eachThreadCols):
		df1 = missingValuesMode(i,(i+eachThreadCols),df,colsToMode)
		results.append(df1)
	
	if (numOfCols % maxThreads != 0):
		df2 = missingValuesMode((eachThreadCols * (maxThreads-1)),numOfCols,df,colsToMode)
		results.append(df2)

# wait for all apps to complete
[r.result() for r in results]

newlist = []
for i in results:
	newlist.append(i.result())

for i in newlist:
	dfNew = pd.concat([dfNew, i], axis=1)

#print(dfNew)
dfNew.to_csv (outputDataset, index = False, header=True)
print("Module Completed: Fill Missing Values with Mode")
