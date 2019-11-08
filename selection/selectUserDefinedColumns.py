from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)


@python_app
def selectUserDefinedColumns():
	import pandas as pd
	df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")
	dfConcat = pd.DataFrame()

	selectedColumns = ["GLOBALEVENTID","SQLDATE", "Year", "Actor2Code", "Actor2Name", "Actor2Religion1Code"]


	if (selectedColumns != "all"):
		dfConcat = pd.DataFrame()

		for i in selectedColumns:
		    df_i=df[i]
		    dfAfterUserSelectedColumns=pd.concat([dfConcat, df_i], axis=1)
		    dfConcat=dfAfterUserSelectedColumns

		    dfConcat.to_csv ("/home/amanda/FYP/testcsv/selection.csv", index = False, header=True)

	else:
	    dfConcat = df.to_csv ("/home/amanda/FYP/testcsv/selection.csv", index = False, header=True)


	ret  = "done"
	return ret



print(selectUserDefinedColumns().result())



