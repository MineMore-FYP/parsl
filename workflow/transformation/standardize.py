# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
import pandas
import numpy
import scipy

import parsl
from parsl import load, python_app

import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import dataType


dataframe = pandas.read_csv("/home/kalpani/Documents/FYP/testcsv/test.csv")

colNames = userScript.userDefinedStandardizeColumns

@python_app
def standardize():
	for col in colNames:
		if dataType.dataType(col, dataframe) != "str":
			standardizeColumn = dataframe.filter([col], axis=1)
			dataframe = dataframe.drop(col, axis=1)
		
			array = standardizeColumn.values
			scaler = StandardScaler().fit(array)
			standardized = scaler.transform(array)

			dataframe[col] = standardized
		else:
			print("The column, ", col, "is of type: string. Cannot standardize")


standardize()
dataframe.to_csv ("/home/kalpani/Documents/FYP/testcsv/test4.csv", index = False, header=True)
