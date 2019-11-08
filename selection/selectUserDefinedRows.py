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

from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def selectUserDefinedRows():
	df = pd.read_csv("/home/rajini/FYP/testcsv/test.csv")
	print(userScript.selectFromRow)
	for key, value in userScript.selectFromRow.items():
		selectValues = []
		n = 0

		while n < len(userScript.selectFromRow[key]):
			selectValues.append(userScript.selectFromRow[key][n])
			n = n+1
		for i in selectValues:
			print(i)
			print(key)
			dfAfterUserSelectedRows = df[df[key] == i]
			df = dfAfterUserSelectedRows


	dfAfterUserSelectedRows.to_csv ("/home/rajini/FYP/testcsv/rowSelection.csv", index = False, header=True)

	ret  = "done"
	return ret


print(selectUserDefinedRows().result())
