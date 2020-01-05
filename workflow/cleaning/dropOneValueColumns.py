#drop unique column

from parsl import load, python_app

import sys
import os,sys,inspect
import pandas as pd
import numpy as np


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript


@python_app
def dropOneValueColumns(startColIndex, endColIndex, dFrame):
	import pandas as pd
	import numpy as np


	df = pd.DataFrame()
	df = dFrame.iloc[: , np.r_[startColIndex : endColIndex]]  

	for col in df.columns:
		if len(df[col].unique()) == 1:
			print(col)
			df.drop(col,inplace=True,axis=1)

	ret  = df
	return ret


from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor

maxThreads = 8
local_threads = Config(
    executors=[
        ThreadPoolExecutor(
            max_threads=maxThreads,
            label='local_threads'
        )
    ]
)


df = pd.read_csv("/home/amanda/FYP/testcsv/test.csv")
numOfCols = df.shape[1]
print(numOfCols)


dfNew = pd.DataFrame()






dfNew = dropOneValueColumns(0,58,df).result()



dfNew.to_csv ("/home/amanda/FYP/testcsv/dropOneValueColumnsOUTPUT.csv", index = False, header=True)




