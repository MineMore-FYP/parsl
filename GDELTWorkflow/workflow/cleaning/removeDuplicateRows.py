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
import threadconfig



@python_app
def removeDuplicateRows(startRowIndex, endRowIndex, dFrame):

	df = pd.DataFrame()
	df = dFrame.iloc[np.r_[startRowIndex : endRowIndex] , : ]
	dfDroppedDuplicates = df.drop_duplicates()
	dfDroppedDuplicates.reset_index(inplace=True)
	
	return dfDroppedDuplicates



#read csv with defined missing values
df = pd.read_csv("/home/amanda/FYP/testcsv/RFout.csv", index_col = False)
numOfRows = df.shape[0]
print(numOfRows)


dfNew = pd.DataFrame()
maxThreads = threadconfig.maxThreads

#not parallel --> relatively small number of rows here
if numOfRows <= maxThreads:
	df1 = (removeDuplicateRows(0, i+1, df).result())

#parallel
elif numOfRows > maxThreads:
	print("test2")
	if (numOfRows % maxThreads == 0):
		eachThreadRows = numOfRows / maxThreads 
		for i in range (maxThreads):
			df1 = (removeDuplicateRows(i,(i+eachThreadRows),df).result())
			dfNew = pd.concat([dfNew, df1] , axis=0)
		
	else:
		eachThreadRows = numOfRows // (maxThreads-1)
		for i in range (0,(maxThreads-1)*eachThreadRows, eachThreadRows):
			print ("i", i)
			print("i+eachThreadRows", (i+eachThreadRows))
			df1 = (removeDuplicateRows(i, (i+eachThreadRows), df).result())
			dfNew = pd.concat([dfNew, df1], axis=0)

		print("last thread",(eachThreadRows * (maxThreads-1))	)
		df2 = (removeDuplicateRows((eachThreadRows * (maxThreads-1)), numOfRows, df).result())
	
		dfNew = pd.concat([dfNew, df2] , axis=0)




dfNew.drop("index",inplace=True,axis=1)
dfNew.to_csv ("/home/amanda/FYP/testcsv/removeDuplicateRowsOUTPUT.csv", index = False, header=True)
#print(removeDuplicateRows(50,100,df).result())
