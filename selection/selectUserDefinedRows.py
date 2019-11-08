from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)


@python_app
def selectUserDefinedRows():

	# importing pandas module
	import pandas as pd
	import sys
	import os,sys,inspect
	currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parentdir = os.path.dirname(currentdir)
	sys.path.insert(0,parentdir)

	import userScript

	# making data frame from csv file
	

	df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")
	for key, value in userScript.selectFromRow.items():
		selectedValues = []
		n = 0

		while n < len(userScript.selectFromRow[key]):
			selectedValues.append(userScript.selectFromRow[key][n])
			n = n+1
		'''for i in selectedValues:
			print(i)
			print(key)
			dfSelectedRows = df[df[key] == i]
			print(dfSelectedRows)
			df = dfSelectedRows
		'''

		print(selectedValues)
		selectedValues = ["2017", "2018"]
		df.loc[df[key].isin(selectedValues)]
		print(df)

	#dfSelectedRows.to_csv ("/home/amanda/FYP/testcsv/sel.csv", index = False, header=True)
	ret  = "done"
	return ret


print(selectUserDefinedRows().result())
