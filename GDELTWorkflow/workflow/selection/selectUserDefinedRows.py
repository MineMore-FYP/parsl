import pandas as pd
import os.path
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import userScript

currentModule = "selectUserDefinedRows"
df = pd.read_csv("/home/amanda/FYP/gdelt/splitIntoRows.csv")


df2 = df.loc[df['ActorGeo_CountryCode'] == "CE"]
df2.to_csv ("/home/amanda/FYP/gdelt/FINAL.csv", index = False, header=True)
