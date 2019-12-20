import pandas as pd
import os.path
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript2
#df = userScript.inputDataFrame

df = pd.read_csv(userScript2.outputLocation + "addLabelColumn.csv")
outputDataset = userScript2.outputLocation + "assignCountryCode.csv"

country=userScript2.country

def assignCountryCode(df1, c):
	df = df1
	df["country"]=c	
	dfConcat = df.to_csv (outputDataset, index = False, header=True)
	return "Assign FIPS country code done."


assignCountryCode(df, country)
print("Module Completed: Assign FIPS country code")
