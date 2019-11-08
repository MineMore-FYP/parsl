import pandas as pd
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

missing_values = userScript.missingValues

#read csv with defined missing values
df = pd.read_csv(sys.argv[1], na_values = missing_values)
df.to_csv (sys.argv[1], index = False, header=True)
