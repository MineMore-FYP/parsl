import pandas as pd
import numpy as np
import statistics

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import dataType
import userScript

df = pd.read_csv(userScript.outputDataset)
#drop unique columns
numOfRows = df.shape[0]

for col in df.columns:
    if len(df[col].unique()) == numOfRows:
        df.drop(col,inplace=True,axis=1)

if(userScript.modeColumns == "all"):
    #Mode of all columns
    colNames = list(df)
else:
    #Mode of user defined columns
    colNames = userScript.modeColumns


df2 = df
df1 = pd.DataFrame()
for col in colNames:

	df1 = df[col].dropna()
	modeOfCol = statistics.mode(df1)
	df2[col].fillna(modeOfCol, inplace = True)

df2.to_csv(userScript.outputDataset, index = False, header=True)
