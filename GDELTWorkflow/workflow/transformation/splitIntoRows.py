import pandas as pd
import numpy as np

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

df = pd.read_csv("/home/amanda/FYP/testcsv/test2.csv")
columnsToAggregate = userScript.userDefinedColumsToAggregate

import parsl
from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def splitIntoRows(startRowIndex, endRowIndex, dFrame, columnsToAggregate):
	import pandas as pd
	import numpy as np
	df = pd.DataFrame()
	df = dFrame.iloc[np.r_[startRowIndex : endRowIndex] , : ]

	columnList = list(df.columns.values)

	for i in columnsToAggregate:
		column1 = i[0]
		print(i[0])
		#column1index = df.columns.get_loc(column1)
		column2 = i[1]
		#column2index = df.columns.get_loc(column2)
		newColumn = i[2]
		newColumnList = []

		newColumnList = columnList
		newColumnList.remove(column1)
		newColumnList.remove(column2)
		newColumnList.append(newColumn)

		print(newColumnList)
	

		dfNew = pd.DataFrame(columns = newColumnList)
		#print(dfNew)

		for index,row in df.iterrows():

			if row[column1] == row[column2]:
				x = row[column1]
				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd = pd.Series([x], index=[newColumn])
				row = row.append(rowAdd)
				dfNew = dfNew.append(row, ignore_index=True)

			elif not row.notnull()[column1] and not row.notnull()[column2]:
				#print("2")
				print("both null")

			elif row.notnull()[column1] and not row.notnull()[column2]:
				#print("3")
				x = row[column1]
				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd = pd.Series([x], index=[newColumn])
				row = row.append(rowAdd)
				dfNew = dfNew.append(row, ignore_index=True)

			elif row.notnull()[column2] and not row.notnull()[column1]:
				#print("4")
				x = row[column2]
				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd = pd.Series([x], index=[newColumn])
				row = row.append(rowAdd)
				dfNew = dfNew.append(row, ignore_index=True)
			else:
				x = row[column1]
				y = row[column2]

				row = row.drop(labels=[column1,column2])
				#print(row)
				rowAdd1 = pd.Series([x], index=[newColumn])
				rowAdd2 = pd.Series([y], index=[newColumn])	
				row1 = row.append(rowAdd1)
				dfNew = dfNew.append(row1, ignore_index=True)
				row2 = row.append(rowAdd2)
				dfNew = dfNew.append(row2, ignore_index=True)
				print(row)
			


		#print(dfNew)
		return dfNew
		#dfNew.to_csv ("/home/amanda/FYP/testcsv/RFout1.csv", index = False, header=True)


maxDivs = 10
results = []
numOfRows = df.shape[0]

#df1 = splitIntoRows(0,100,df,columnsToAggregate)
#print(df1.result())
'''
if (numOfRows % maxDivs == 0):
	eachDivRows = numOfRows / maxDivs 
	for i in range (maxDivs):
		df1 = splitIntoRows(i,(i+eachDivRows),df,columnsToAggregate)
		results.append(df1)
		#dfNew = pd.concat([dfNew, df1] , axis=0)
		
else:
	eachDivRows = numOfRows // (maxDivs-1)
	for i in range (0,(maxDivs-1)*eachDivRows, eachDivRows):
		print ("i", i)
		print("i+eachDivRows", (i+eachDivRows))
		df1 = splitIntoRows(i, (i+eachDivRows), df, columnsToAggregate)
		results.append(df1)
		#dfNew = pd.concat([dfNew, df1], axis=0)

	print("last division",(eachDivRows * (maxDivs-1))	)
	df2 = splitIntoRows((eachDivRows * (maxDivs-1)), numOfRows, df, columnsToAggregate)
	results.append(df2)


newlist = []	
for i in results:
	newlist.append(i.result())

for i in newlist:
	
	dfNew = pd.concat([dfNew, i], axis=0)


#dfNew = newlist[0]
print(dfNew)

dfNew.drop("index",inplace=True,axis=1)
print(dfNew)

dfNew.to_csv ("/home/amanda/FYP/testcsv/splittt.csv", index = False, header=True)
#print(removeDuplicateRows(50,100,df).result())
'''
