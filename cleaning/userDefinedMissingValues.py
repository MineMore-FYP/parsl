from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

@python_app
def userDefinedMissingValues():
    import pandas as pd
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import userScript

    missing_values = userScript.missingValues

    #read csv with defined missing values
    df = pd.read_csv(userScript.inputDataset, na_values = missing_values)

    df.to_csv ("/home/rajini/FYP/testcsv/userDefinedMissingValuesOUTPUT.csv", index = False, header=True)
    
    ret  = "Set user defined missing values complete"
    return ret

print(userDefinedMissingValues().result())
