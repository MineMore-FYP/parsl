import pandas as pd
import numpy as np
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import dataType
import userScript

df = pd.read_csv(sys.argv[1])

if(userScript.interpolateColumns == "all"):
    #Interpolate all integer columns
    colNames = list(df)
else:
    #Interpolate user defined columns
    colNames = userScript.interpolateColumns

for col in colNames:
    if dataType.dataType(col, df) != "str":
        # to interpolate the missing values
        df[col] = df[col].interpolate(method ='linear', limit_direction ='forward')
    else:
        #print("The column, ", col, "is of type: string. Cannot interpolate")
        df.to_csv (sys.argv[1], index = None, header=True)
