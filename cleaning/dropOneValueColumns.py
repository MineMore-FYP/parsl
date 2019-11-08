#drop unique column

from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def dropOneValueColumns():
    import pandas as pd
    import numpy as np
    import sys
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import userScript

    df = pd.read_csv(userScript.inputDataset)

    for col in df.columns:
        if len(df[col].unique()) == 1:
            df.drop(col,inplace=True,axis=1)
            print(col)

    df.to_csv ("/home/rajini/FYP/testcsv/dropOneValueColumnsOUTPUT.csv", index = False, header=True)

    ret  = "Drop One Value Columns complete"
    return ret

print(dropOneValueColumns().result())
