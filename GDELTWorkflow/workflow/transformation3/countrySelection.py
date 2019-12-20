import pandas as pd

import os,sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript3

path = userScript3.outputLocation

#read combined csv
df = pd.read_csv(path + "splitIntoRows.csv")
print(df)

#select specific country records
df2 = df.loc[df['ActorGeo_CountryCode'] == userScript3.ActorGeo_CountryCode]
print(df2)

#write to a new csv
df2.to_csv(path + "dropCountry.csv", index = False, header=True)


