import pandas as pd

import os,sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

path = userScript.datafilesLocation

#read combined csv
df = pd.read_csv(path + "combined.csv")
print(df)

#select specific country records
df2 = df.loc[(df['Actor1CountryCode'] == userScript.Actor1CountryCode) & (df['Actor2CountryCode'] == userScript.Actor2CountryCode)]
print(df2)

#write to a new csv
df2.to_csv(path + "dropCountry.csv", index = False, header=True)


