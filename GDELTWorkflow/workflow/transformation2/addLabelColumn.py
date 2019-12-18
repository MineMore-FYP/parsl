import pandas as pd
import os.path
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript2
#df = userScript.inputDataFrame

df = pd.read_csv(userScript2.outputLocation + "missingValuesMode.csv")
outputDataset = userScript2.outputLocation + "addLabelColumn.csv"

labelValue=userScript2.labelValue

def addLabelColumnColumns(df1, lv):
	df = df1
	df["label"]=lv	
	dfConcat = df.to_csv (outputDataset, index = False, header=True)
	return "Appending label column done."


addLabelColumnColumns(df, labelValue)
print("Module Completed: Append label column")
