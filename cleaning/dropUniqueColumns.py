from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def dropUniqueColumns():
    import pandas as pd
    import numpy as np
    import sys
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import userScript

    df = pd.read_csv(userScript.inputDataset)
    numOfRows = df.shape[0]

    for col in df.columns:
        if len(df[col].unique()) == numOfRows:
            df.drop(col,inplace=True,axis=1)

    df.to_csv("/home/rajini/FYP/testcsv/dropUniqueColumnsOUTPUT.csv", index = False, header=True)

    ret  = "Drop Unique Columns complete"
    return ret

print(dropUniqueColumns().result())
