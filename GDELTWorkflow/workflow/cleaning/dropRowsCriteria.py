from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def dropRowsCriteria():
    import pandas as pd
    import numpy as np
    import sys
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import userScript

    df = pd.read_csv("/home/amanda/FYP/ds/combined.csv")

    numOfColumns = len(df.columns)
    #user defined percentage
    maxPercentageOfMissingValues= userScript.userDefinedRowPercentage
    threshold = (numOfColumns * maxPercentageOfMissingValues)/100


    df = df.dropna(thresh=threshold)
    df.to_csv ("/home/amanda/FYP/testcsv/droprow.csv", index = False, header=True)

    ret  = "Drop Rows according to user defined missing value percentage complete"
    return ret

print(dropRowsCriteria().result())
