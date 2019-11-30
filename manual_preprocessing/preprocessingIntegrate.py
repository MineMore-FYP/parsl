import os
import glob
import pandas as pd
import csv
import numpy as np

import preprocessingRecords

# read original csv generated from gdelt
dfOriginal = pd.read_csv("/home/rajini/output.csv", header=0)

# read manual csv with riot information
dfManual = pd.read_csv("/home/rajini/Desktop/riots/combinedRiots.csv", header=0)

# number of rows in gdelt generated dataset
numberOfRowsOriginal = dfOriginal.shape[0]

# number of rows in manually generated dataset
numberOfRowsManual = dfManual.shape[0]

# insert new label column with default value of zero
dfOriginal['year']=0	
dfOriginal['month']=0	
dfOriginal['date']=0	
dfOriginal['label']=0	

# iterating over rows of df original and generating values for Y,M,D from SQLDATE
for i, j in dfOriginal.iterrows(): 
	sqldate = dfOriginal.loc[i][0]
	strSqlDate = str(sqldate) 

	year = strSqlDate[0:4] 
	month = strSqlDate[4:6] 
	date = strSqlDate[6:8] 

	dfOriginal.set_value([i], ['year'], year)
	dfOriginal.set_value([i], ['month'], month)
	dfOriginal.set_value([i], ['date'], date)	

def generateMonthlyDf(year,month):
	print("Hello")

count=0
for i in preprocessingRecords.years:
	for j in range (12):
		count=count+1
		print(count)

print(dfOriginal)

#dfOriginal.to_csv("/home/rajini/Desktop/riots/labelledOriginalData.csv", sep=',', encoding='utf-8', index=False, header=True)

'''
# iterate over all records from gdelt dataset
for i in range (numberOfRowsOriginal):
	#print(dfOriginal.loc[i][:])
	for j in range (numberOfRowsManual):
		if (dfOriginal.loc[i][0]==dfManual.loc[j][0]):
			if (dfOriginal.loc[i][1]==dfManual.loc[j][1]):
				print("Hello")

'''
