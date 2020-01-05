# Rescale data (between 0 and 1)
import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler

import parsl
from parsl import load, python_app

import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import dataType

df = pandas.read_csv("/home/kalpani/Documents/FYP/testcsv/test.csv")

print(userScript.userDefinedRescaleColumns.items())

@python_app
def rescale():
	for key, value in userScript.userDefinedRescaleColumns.items():
		if dataType.dataType(key, df) != "str":
			lowerBound = value[0]
			upperBound = value[1]
			col = key
			scaler = MinMaxScaler(feature_range=(lowerBound, upperBound))

			rescaleColumn = df.filter([col], axis=1)
			df = df.drop(col, axis=1)

			array = rescaleColumn.values
			rescaled = scaler.fit_transform(array)

			df[col] = rescaled
		else:
			print("The column, ", col, "is of type: string. Cannot rescale")	    

rescale()
df.to_csv ("/home/kalpani/Documents/FYP/testcsv/test3.csv", index = False, header=True)
