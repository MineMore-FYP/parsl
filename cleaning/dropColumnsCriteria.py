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

#read csv with defined missing values
df = pd.read_csv(userScript.inputDataset)
numOfCols = df.shape[1]
print(numOfCols)
eachThreadCols = numOfCols//10

#prints 0,1 cols
#print(df.iloc[: , [0, 2]])
#print(df.iloc[ : , numOfCols-1 ])

#user defined percentage of maximum of allowed missing values
maxPercentageOfMissingValues= userScript.userDefinedColPercentage


@python_app
def dropColumnsCriteria(startColIndex, endColIndex, dFrame, maxPercentage, filename):

	import pandas as pd
	import numpy as np
	import sys
	import os,sys,inspect
	
	#function to count thr number of missing values in a given column
	def countMissingValues(colName, df):
	  dfCol = df[colName]
	  return dfCol.isnull().sum()
	

	df = dFrame.iloc[: , [startColIndex, endColIndex]]
	print(df)

	colNames = list(df)
	noOfRows = df.shape[0]
	#print("Total Number of Rows : ",noOfRows, "\n")
	#print("Column Name : ", colNames, "\n")

	dfMissingValueCriteriaDropped=df
	
	for i in colNames:
	  noMissingValues = countMissingValues(i,df)

	  if ((noMissingValues/noOfRows)>(maxPercentage/100)):
	    dfMissingValueCriteriaDropped = dfMissingValueCriteriaDropped.drop(i, axis=1)

	dfMissingValueCriteriaDropped.to_csv ("/home/amanda/FYP/testcsv/"+filename+".csv", index = False, header=True)
	ret  = "Drop Columns according to user defined missing value percentage complete"
	ret1 = dfMissingValueCriteriaDropped
	return ret

































'''
@python_app
def dropColumnsCriteria(startColIndex, endColIndex, dFrame):

	import pandas as pd
	import numpy as np
	import sys
	import os,sys,inspect
	currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parentdir = os.path.dirname(currentdir)
	sys.path.insert(0,parentdir)

	import userScript

	#function to count thr number of missing values in a given column
	def countMissingValues(colName, df):
	  dfCol = df[colName]
	  return dfCol.isnull().sum()
	

	#user defined percentage of maximum of allowed missing values
	maxPercentageOfMissingValues= userScript.userDefinedColPercentage

	colNames = list(df)
	noOfRows = df.shape[0]
	#print("Total Number of Rows : ",noOfRows, "\n")
	#print("Column Name : ", colNames, "\n")

	dfMissingValueCriteriaDropped=df
	for i in colNames:
	  noMissingValues = countMissingValues(i,df)

	  if ((noMissingValues/noOfRows)>(maxPercentageOfMissingValues/100)):
	    dfMissingValueCriteriaDropped = dfMissingValueCriteriaDropped.drop(i, axis=1)

	dfMissingValueCriteriaDropped.to_csv ("/home/amanda/FYP/testcsv/cleaning.csv", index = False, header=True)
	ret  = "Drop Columns according to user defined missing value percentage complete"
	return ret
'''

print(dropColumnsCriteria(8,8,df,maxPercentageOfMissingValues, "cleaning1").result())
#print(dropColumnsCriteria(25,50,df,maxPercentageOfMissingValues, "cleaning2").result())





