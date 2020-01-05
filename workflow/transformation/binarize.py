# binarization
from sklearn.preprocessing import Binarizer
import pandas as pd
import numpy
import scipy

import parsl
from parsl import load, python_app

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import dataType

df = pd.read_csv("/home/kalpani/Documents/FYP/testcsv/test.csv",engine = 'python') # reemoved , names=names

@python_app
def binarize():
	for key, value in userScript.userDefinedBinarizeColumns.items():
		if dataType.dataType(key, df) != "str":
			#user defined threshold
			userThreshold= value[0]
			col = key

			binarizeColumn = df.filter([col], axis=1)
			df = df.drop(col, axis=1)

			array = binarizeColumn.values
			binarizer = Binarizer(threshold=userThreshold).fit(array)
			binary = binarizer.transform(array)

			df[col] = binary
		else:
			print("The column, ", col, "is of type: string. Cannot binarize")


binarize()
df.to_csv ("/home/kalpani/Documents/FYP/testcsv/test2.csv", index = False, header=True)
