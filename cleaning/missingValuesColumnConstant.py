import pandas as pd
import numpy as np

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import dataType

df = pd.read_csv(sys.argv[1])

od = missingValueCons

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

df.to_csv (sys.argv[1], index = False, header=True)
