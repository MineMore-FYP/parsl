import pandas as pd
from parsl import load, python_app
from parsl.configs.local_threads import config
#load(config)


from python1 import *
from python2 import *


@python_app
def fun_df():
	return df

@python_app
def app_dropColumns(inputs=[]):
    dfUserDroppedCols = df.drop(inputs, axis=1)
    return dfUserDroppedCols



#df1 = fun_df()

#print(df1.result())
	
df_final = app_dropColumns(dropCols)
print(df_final.result())


