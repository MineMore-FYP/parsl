from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def removeDuplicateRows():
    import pandas as pd
    import numpy as np
    import sys
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import userScript

    df = pd.read_csv(userScript.inputDataset)

    dfDroppedDuplicates = df.drop_duplicates()
    dfDroppedDuplicates.reset_index(inplace=True)

    dfDroppedDuplicates.to_csv ("/home/rajini/FYP/testcsv/removeDuplicateRowsOUTPUT.csv", index = False, header=True)

    ret  = "Remove duplicate rows complete"
    return ret

print(removeDuplicateRows().result())
