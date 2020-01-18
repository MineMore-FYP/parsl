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
import parslConfig
import dataType

currentModule = "rescale"
workflowNumber = sys.argv[1]

if workflowNumber == "1":
	orderOfModules = userScript.orderOfModules1
	inputDataset = userScript.inputDataset1
	outputLocation = userScript.outputLocation1
	dropCols = userScript.dropCols1
elif workflowNumber == "2":
	orderOfModules = userScript.orderOfModules2
	inputDataset = userScript.inputDataset2
	outputLocation = userScript.outputLocation2
	dropCols = userScript.dropCols2
elif workflowNumber == "3":
	orderOfModules = userScript.orderOfModules3
	inputDataset = userScript.inputDataset3
	outputLocation = userScript.outputLocation3
	dropCols = userScript.dropCols3
	userDefinedRescaleColumns = userScript.userDefinedRescaleColumns


df = pd.DataFrame()
for i in range(len(orderOfModules)):
	#print(orderOfModules[i])
	if currentModule == orderOfModules[i]:
		if i == 0:
			df = pd.read_csv(inputDataset)
			break
		else:
			previousModule = orderOfModules[i-1]
			df = pd.read_csv(outputLocation + previousModule + ".csv")
			break

outputDataset = outputLocation + currentModule + ".csv"

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
