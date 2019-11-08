import pandas as pd
import numpy as np
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

df = pd.read_csv(sys.argv[1])

numOfColumns = len(df.columns)
#user defined percentage
maxPercentageOfMissingValues= userScript.userDefinedRowPercentage
threshold = (numOfColumns * maxPercentageOfMissingValues)/100


df = df.dropna(thresh=threshold)
df.to_csv (sys.argv[1], index = False, header=True)
