import pandas as pd
import numpy as np

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

df = pd.read_csv("/home/amanda/FYP/ds/combined.csv")
columnsToSplit = userScript.userDefinedColumsToSplit

actor_CountryCode = []

for i in columnsToSplit:
	column1 = i[0]
	column2 = i[1]

	for index,row in df.iterrows():
		if row[column1] == row[column2]:
			actor_CountryCode.append(row[column1])
#			print(row[column1], row[column2])
		elif not row.notnull()[column1] and not row.notnull()[column2]:
			#print ("both null")
		elif row.notnull()[column1] and not row.notnull()[column2]:
			actor_CountryCode.append(row[column1])
			#print(row[column1], row[column2])
			
		elif row.notnull()[column2] and not row.notnull()[column1]:
			actor_CountryCode.append(row[column1])
			#print(row[column1], row[column2])

		else:
			actor_CountryCode1 = row[column1]
			actor_CountryCode2 = row[column2]
	

	#drop both cols
	df = df.drop([column1, column2], axis = 1)
	#concat with actor_CountryCode
	df["ActorGeo_CountryCode"] = actor_CountryCode



#dfObj.append({'Name' : 'Sahil' , 'Age' : 22} , ignore_index=True)
	
