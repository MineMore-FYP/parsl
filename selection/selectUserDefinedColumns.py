from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)


@python_app
def selectUserDefinedColumns():
	import pandas as pd
	import os.path
	import os,sys,inspect
	currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parentdir = os.path.dirname(currentdir)
	sys.path.insert(0,parentdir)

	import userScript

	df = pd.read_csv(userScript.inputDataset)
	dfConcat = pd.DataFrame()

	#selectedColumns = ["GLOBALEVENTID","SQLDATE", "Year", "Actor2Code", "Actor2Name", "Actor2Religion1Code"]

	selectedColumns = userScript.selectColumns	

	if (selectedColumns != "all"):
		dfConcat = pd.DataFrame()

		for i in selectedColumns:
		    df_i=df[i]
		    dfAfterUserSelectedColumns=pd.concat([dfConcat, df_i], axis=1)
		    dfConcat=dfAfterUserSelectedColumns

		    dfConcat.to_csv ("/home/amanda/FYP/testcsv/selection.csv", index = False, header=True)

	else:
	    dfConcat = df.to_csv ("/home/amanda/FYP/testcsv/selection.csv", index = False, header=True)


	ret  = "Select User Defined Columns complete"
	return ret



print(selectUserDefinedColumns().result())



