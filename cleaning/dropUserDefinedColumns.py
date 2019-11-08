from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def dropUserDefinedColumns():
    import pandas as pd
    import numpy as np
    import sys
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import userScript

    df = pd.read_csv(userScript.inputDataset)

    #dropColumns list from userScript
    dropCols = userScript.dropColumns

    dfUserDroppedCols = df.drop(dropCols, axis=1)

    dfUserDroppedCols.to_csv ("/home/rajini/FYP/testcsv/dropUserDefinedColumnsOUTPUT.csv", index = False, header=True)

    ret  = "Drop User Defined Columns complete"
    return ret

print(dropUserDefinedColumns().result())

