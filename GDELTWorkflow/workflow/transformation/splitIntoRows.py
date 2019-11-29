import pandas as pd
import numpy as np

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

df = pd.read_csv("/home/amanda/FYP/testcsv/RFout.csv")
columnsToAggregate = userScript.userDefinedColumsToAggregate
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
	#newColumnList.append(newColumn)

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
			


	print(dfNew)

	dfNew.to_csv ("/home/amanda/FYP/testcsv/RFout1.csv", index = False, header=True)
#dfObj.append({'Name' : 'Sahil' , 'Age' : 22} , ignore_index=True)
	
