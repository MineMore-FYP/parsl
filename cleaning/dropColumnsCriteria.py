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


#read csv with defined missing values
df = pd.read_csv(sys.argv[1])

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

dfMissingValueCriteriaDropped.to_csv (sys.argv[1], index = False, header=True)
