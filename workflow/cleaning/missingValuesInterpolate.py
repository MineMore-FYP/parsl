from parsl import load, python_app

@python_app
def missingValuesInterpolate():
    import pandas as pd
    import numpy as np
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    import dataType
    import userScript

    df = pd.read_csv(userScript.inputDataset)

    if(userScript.interpolateColumns == "all"):
        #Interpolate all integer columns
        colNames = list(df)
    else:
        #Interpolate user defined columns
        colNames = userScript.interpolateColumns

    df2 = df
    df1 = pd.DataFrame()
    
    for col in colNames:
        if dataType.dataType(col, df) != "str":
            # to interpolate the missing values
            print(col)
            df[col] = df[col].interpolate(method ='linear', limit_direction ='forward')
        else:
            print("The column, ", col, "is of type: string. Cannot interpolate")
        
    df.to_csv ("/home/rajini/FYP/testcsv/missingValuesInterpolateOUTPUT.csv", index = None, header=True)

    ret  = "Missing values Interpolate complete"
    return ret

print(missingValuesInterpolate().result())

        
