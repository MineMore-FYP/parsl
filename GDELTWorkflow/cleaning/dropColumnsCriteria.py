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

#prints 0,1 cols
#print(df.iloc[: , np.r_[0 : 3]])
#print(df.iloc[ : , numOfCols-1 ])

#user defined percentage of maximum of allowed missing values
maxPercentageOfMissingValues= userScript.userDefinedColPercentage


@python_app
def dropColumnsCriteria(startColIndex, endColIndex, dFrame, maxPercentage):

	import pandas as pd
	import numpy as np
	import sys
	import os,sys,inspect
	
	#function to count thr number of missing values in a given column
	def countMissingValues(colName, df):
	  dfCol = df[colName]
	  return dfCol.isnull().sum()
	
	df = pd.DataFrame()

	df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]
	#print(df)

	colNames = list(df)
	noOfRows = df.shape[0]
	#print("Total Number of Rows : ",noOfRows, "\n")
	#print("Column Name : ", colNames, "\n")

	dfMissingValueCriteriaDropped=df
	
	for i in colNames:
	  noMissingValues = countMissingValues(i,df)

	  if ((noMissingValues/noOfRows)>(maxPercentage/100)):
	    dfMissingValueCriteriaDropped = dfMissingValueCriteriaDropped.drop(i, axis=1)

	
	ret = dfMissingValueCriteriaDropped
	return ret

 

from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor

maxThreads = 8
local_threads = Config(
    executors=[
        ThreadPoolExecutor(
            max_threads=maxThreads,
            label='local_threads'
        )
    ]
)




#read csv with defined missing values
df = pd.read_csv(userScript.inputDataset)
numOfCols = df.shape[1]
print(numOfCols)

lasThreadCols = 0

dfNew = pd.DataFrame()


if (numOfCols % maxThreads == 0):
	eachThreadCols = numOfCols / maxThreads 
	for i in range (maxThreads):
		df1 = (dropColumnsCriteria(i,(i+eachThreadCols),df,maxPercentageOfMissingValues).result())
		dfNew = pd.concat(dfNew, df1)
		
else:
	eachThreadCols = numOfCols // (maxThreads-1)
	lasThreadCols = numOfCols % maxThreads
	for i in range (0,(maxThreads-1)*eachThreadCols, eachThreadCols):
		print ("i", i)
		print("i+eachThreadCols", (i+eachThreadCols))
		df1 = (dropColumnsCriteria(i,(i+eachThreadCols),df,maxPercentageOfMissingValues).result())
		dfNew = pd.concat([dfNew, df1], axis=1)

	print("last thread",(eachThreadCols * (maxThreads-1))	)
	df2 = (dropColumnsCriteria((eachThreadCols * (maxThreads-1)),lasThreadCols + (eachThreadCols * (maxThreads-1)),df,maxPercentageOfMissingValues).result())
	
	dfNew = pd.concat([dfNew, df2] , axis=1)
 



#***********************the following runs in parallel. but needs to be put into a for loop. HOW do we do this?******************************
#df1 = (dropColumnsCriteria(0,8,df,maxPercentageOfMissingValues).result())
#df2 = (dropColumnsCriteria(8,59,df,maxPercentageOfMissingValues).result())


#dfNew = pd.concat([df1, df2], axis=1)
print(dfNew)
dfNew.to_csv ("/home/amanda/FYP/testcsv/cleaning.csv", index = False, header=True)
#43 cols



df3 = (dropColumnsCriteria(0,59,df,maxPercentageOfMissingValues).result())
df3.to_csv ("/home/amanda/FYP/testcsv/cleaning1.csv", index = False, header=True)
print (df3)
#43 cols







