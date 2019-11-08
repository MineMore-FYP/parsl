#encoding
import pandas as pd
import numpy as np
import sys
# Import LabelEncoder
from sklearn import preprocessing
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

df = pd.read_csv(sys.argv[1])

columnNames = userScript.userDefinedEncodeColumns

for col in columnNames:
    encodeColumn=df[col].astype(str)
    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    encodedData=le.fit_transform(encodeColumn)

    df = df.drop(col, axis=1)

    df[col] = encodedData

    #print(encodedData)

df.to_csv (sys.argv[1], index = False, header=True)
print("Encoding done!")
