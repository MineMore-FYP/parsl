def selectUserDefinedColumns:
	import pandas as pd
	df = "/home/amanda/FYP/testcsv/test.csv"

	selectedColumns = userScript.selectColumns

	if (selectedColumns != "all"):
		dfConcat = pd.DataFrame()

		for i in selectedColumns:
		    df_i=df[i]
		    dfAfterUserSelectedColumns=pd.concat([dfConcat, df_i], axis=1)
		    dfConcat=dfAfterUserSelectedColumns

		    dfConcat.to_csv (userScript.outputDataset, index = False, header=True)

	else:
	    dfConcat = df.to_csv (userScript.outputDataset, index = False, header=True)
