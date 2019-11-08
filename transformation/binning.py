#Binning for integer features:
import pandas as pd
import numpy as np
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import dataType

df = pd.read_csv(sys.argv[1])
columnNames = userScript.userDefinedBinningColumns

for col in columnNames:
    #df_no_missing = data[colName].dropna()
    binArray = np.array([])

    for row in df_no_missing:
       intValue = int(row)
       binArray = np.append(binArray, intValue)

    binArray[0]
    #pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)
    #pd.cut(np.ones(5), 4, labels=False)

    pd.cut(binArray, 3, labels=["0", "1","2"])

    #drop na already done by this stage.
