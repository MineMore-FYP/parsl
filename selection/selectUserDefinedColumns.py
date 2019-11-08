from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)


@python_app
def selectUserDefinedColumns():
	import pandas as pd
	df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")
	dfConcat = pd.DataFrame()

	selectedColumns = ["GLOBALEVENTID","SQLDATE", "Year", "Actor2Code", "Actor2Name", "Actor2Religion1Code", "Actor2Type1Code", "EventCode", "EventRootCode", "QuadClass", "GoldsteinScale", "NumMentions", "NumSources", "NumArticles", "AvgTone", "Actor2Geo_FullName"]


#####FIX HERE########

	for i in selectedColumns:
	    df_i=df[i]
	    dfAfterUserSelectedColumns=pd.concat([dfConcat, df_i], axis=1)
	    dfConcat=dfAfterUserSelectedColumns
	dfConcat = df.to_csv ("/home/amanda/FYP/testcsv/selection.csv", index = False, header=True)
	
	returnval = "Select user defined cols done"
	return returnval

st = selectUserDefinedColumns()

print("test")
print(st.result())
