from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)
from collections import OrderedDict

selectFromRow = OrderedDict()
selectFromRow['Year'] = [2018, 2019]

@python_app
def selectUserDefinedRows():
	import pandas as pd
	df = pd.read_csv("/home/rajini/FYP/testcsv/test.csv")
	for key, value in selectFromRow.items():
		selectValues = []
		n = 0

		while n < len(selectFromRow[key]):
			selectValues.append(selectFromRow[key][n])
			n = n+1
		for i in selectValues:
			print(i)
			print(key)
			dfAfterUserSelectedRows = df[df[key] == i]
			df = dfAfterUserSelectedRows


	dfAfterUserSelectedRows.to_csv ("/home/rajini/FYP/testcsv/rowSelection.csv", index = False, header=True)

st = selectUserDefinedRows()

print("test")
print(st.result())
