#encoding
import pandas as pd
import numpy as np
import sys

import parsl
from parsl import load, python_app
from parsl.configs.local_threads import config

load(config)

# Import LabelEncoder
from sklearn import preprocessing
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

df = pd.read_csv("/home/kalpani/Documents/FYP/testcsv/test.csv")

columnNames = userScript.userDefinedEncodeColumns

@python_app
def encode():
	for col in columnNames:
		encodeColumn=df[col].astype(str)
		#creating labelEncoder
		le = preprocessing.LabelEncoder()
		# Converting string labels into numbers.
		encodedData=le.fit_transform(encodeColumn)

		df = df.drop(col, axis=1)

		df[col] = encodedData

		#print(encodedData)

encode()
df.to_csv ("/home/kalpani/Documents/FYP/testcsv/test5.csv", index = False, header=True)
print("Encoding done!")
