# importing pandas module
import pandas as pd
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript



# making data frame from csv file
#drop values from index label

df = pd.read_csv(sys.argv[1])

for key, value in userScript.dropFromRow.items():
	deleteValues = []
	n = 0

	while n < len(userScript.dropFromRow[key]):
		deleteValues.append(userScript.dropFromRow[key][n])
		n = n+1
	for i in deleteValues:
		print(i)
		print(key)
		dfAfterUserDroppedRows = df[df[key] != i]
		df = dfAfterUserDroppedRows


dfAfterUserDroppedRows.to_csv (sys.argv[1], index = False, header=True)
