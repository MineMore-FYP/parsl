from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def missingValuesMode():
    import pandas as pd
    import numpy as np
    import statistics
    from statistics import mode, StatisticsError

    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import dataType
    import userScript

    df = pd.read_csv(userScript.inputDataset)
    #drop unique columns
    numOfRows = df.shape[0]

    for col in df.columns:
        if len(df[col].unique()) == numOfRows:
            df.drop(col,inplace=True,axis=1)

    if(userScript.modeColumns == "all"):
        #Mode of all columns
        colNames = list(df)
    else:
        #Mode of user defined columns
        colNames = userScript.modeColumns

    df2 = df
    df1 = pd.DataFrame()
    
    for col in colNames:
        try:
            df1 = df[col].dropna()
            modeOfCol = statistics.mode(df1)
            df2[col].fillna(modeOfCol, inplace = True)
        except StatisticsError:
            print(col)
            print ("No unique mode found")

    df2.to_csv("/home/rajini/FYP/testcsv/missingValuesModeOUTPUT.csv", index = False, header=True)

    ret  = "Missing values Mode complete"
    return ret

print(missingValuesMode().result())
