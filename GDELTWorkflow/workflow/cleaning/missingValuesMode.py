from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)


import pandas as pd
import numpy as np
import statistics
from statistics import mode, StatisticsError

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import dataType
import userScript
import threadconfig

colsToMode = userScript.modeColumns
df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")

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





maxThreads = threadconfig.maxThreads

numOfCols = df.shape[1]
print(numOfCols)

lasThreadCols = 0
dfNew = pd.DataFrame()

#one col per thread
if numOfCols <= maxThreads:
	for i in range (maxThreads):
		df1 = (missingValuesMode(0, i+1, df, colsToMode).result())
		dfNew = pd.concat([dfNew, df1] , axis=1)


elif numOfCols > maxThreads:
	print("test2")
	if (numOfCols % maxThreads == 0):
		eachThreadCols = numOfCols / maxThreads 
		for i in range (maxThreads):
			df1 = (missingValuesMode(i,(i+eachThreadCols),df,colsToMode).result())
			dfNew = pd.concat([dfNew, df1] , axis=1)
		
	else:
		eachThreadCols = numOfCols // (maxThreads-1)
		lasThreadCols = numOfCols % (maxThreads-1)
		for i in range (0,(maxThreads-1)*eachThreadCols, eachThreadCols):
			print ("i", i)
			print("i+eachThreadCols", (i+eachThreadCols))
			df1 = (missingValuesMode(i,(i+eachThreadCols),df,colsToMode).result())
			dfNew = pd.concat([dfNew, df1], axis=1)

		print("last thread",(eachThreadCols * (maxThreads-1))	)
		df2 = (missingValuesMode((eachThreadCols * (maxThreads-1)),numOfCols,df,colsToMode).result())
	
		dfNew = pd.concat([dfNew, df2] , axis=1)





print(dfNew)
dfNew.to_csv ("/home/amanda/FYP/testcsv/mode.csv", index = False, header=True)



