import pandas as pd
import os.path
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import userScript

currentModule = "selectUserDefinedColumns"
df = pd.DataFrame()
for i in range(len(userScript.orderOfModules)):
	print(userScript.orderOfModules[i])
	if currentModule == userScript.orderOfModules[i]:
		if i == 0:
			df = pd.read_csv(userScript.inputDataset)
			break
		else:
			previousModule = userScript.orderOfModules[i-1]
			df = pd.read_csv(userScript.outputLocation + previousModule + ".csv")
			break

outputDataset = userScript.outputLocation + currentModule + ".csv"
selectedColumns = userScript.selectColumns


def selectUserDefinedColumns(df1):
	df = df1
	if (selectedColumns != "all"):
		dfConcat = pd.DataFrame()

		for i in selectedColumns:
		    #print(i)
		    #print(df[i])
		    df_i=df[i]
		    dfAfterUserSelectedColumns=pd.concat([dfConcat, df_i], axis=1)
		    dfConcat=dfAfterUserSelectedColumns
		    dfConcat.to_csv (outputDataset, index = False, header=True)

	else:
		dfConcat = df.to_csv (outputDataset, index = False, header=True)
	return "Selection of user defined columns done."


selectUserDefinedColumns(df)
print("Module Completed: Select User Defined Columns")
