from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)



###############################FIX FOR DICTIONARIES#######################################	
@python_app
def missingValuesColumnConstant():

	import pandas as pd
	import numpy as np

	import os,sys,inspect
	currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parentdir = os.path.dirname(currentdir)
	sys.path.insert(0,parentdir)

	import userScript
	import dataType

	df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")

	od = userScript.missingValueCons

	for col, value in od.items():
	  if dataType.dataType(col, df) == "int":
	    if type(value)== "int":
	      df[col].fillna(value, inplace = True)
	  else if dataType.dataType(col, df) == "str":
	    if type(value)== "str":
	      df[col].fillna(value, inplace = True)
	  else if dataType.dataType(col, df) == "float":
	    if type(value)== "float":
	      df[col].fillna(value, inplace = True)

	df.to_csv ("/home/amanda/FYP/testcsv/missingVal.csv", index = False, header=True)

	ret  = "Fill missing values according to user defined constant complete"
	return ret

print(missingValuesColumnConstant().result())
