import os
import glob
import pandas as pd
import csv
import numpy as np

# INDICATE UNREST EVENTS FOR THREE DAYS PRIOR TO ACTUAL UNREST EVENT

# read original csv generated from gdelt
dfFinal = pd.read_csv("/home/rajini/Desktop/riots/finalCSVOut.csv", header=0)

for i, j in dfFinal.iterrows():
	year=dfFinal.loc[i]["year"]
	month=dfFinal.loc[i]["month"]
	date=dfFinal.loc[i]["date"]
	country=dfFinal.loc[i]["ActorGeo_CountryCode"]
	quadClass=dfFinal.loc[i]["QuadClass"]
	label=dfFinal.loc[i]["label"] 
	if label==1:
		count=0

		if date>3:
			for i in range (date-3,date):
				newRow={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":i,"label":1}
				dfFinal=dfFinal.append(newRow, ignore_index=True)
		
		if date==3:
			if month in range (2,13):
				for i in range (date-3,date-1):
					newRow={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":i,"label":1}
					dfFinal=dfFinal.append(newRow, ignore_index=True)
				month=month-1
				newRowA={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":31,"label":1}
				dfFinal=dfFinal.append(newRowA, ignore_index=True)
			if month==1:
				year=year-1
				newRowB={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":12,"date":31,"label":1}
				dfFinal=dfFinal.append(newRowB, ignore_index=True)

		if date==2:
			if month in range (2,13):
				for i in range (date-3,date-1):
					newRow={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":i,"label":1}
					dfFinal=dfFinal.append(newRow, ignore_index=True)
				month=month-1
				newRowA={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":31,"label":1}
				dfFinal=dfFinal.append(newRowA, ignore_index=True)
				newRowB={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":30,"label":1}
				dfFinal=dfFinal.append(newRowB, ignore_index=True)
			
			if month==1:
				year=year-1
				newRowC={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":12,"date":31,"label":1}
				dfFinal=dfFinal.append(newRowC, ignore_index=True)
				newRowD={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":12,"date":30,"label":1}
				dfFinal=dfFinal.append(newRowD, ignore_index=True)

		if date==1:
			if month in range (2,13):
				month=month-1
				newRowA={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":31,"label":1}
				dfFinal=dfFinal.append(newRowA, ignore_index=True)
				newRowB={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":30,"label":1}
				dfFinal=dfFinal.append(newRowB, ignore_index=True)
				newRowC={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":month,"date":29,"label":1}
				dfFinal=dfFinal.append(newRowC, ignore_index=True)
			
			if month==1:
				year=year-1
				newRowD={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":12,"date":31,"label":1}
				dfFinal=dfFinal.append(newRowD, ignore_index=True)
				newRowE={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":12,"date":30,"label":1}
				dfFinal=dfFinal.append(newRowE, ignore_index=True)
				newRowF={"SQLDATE":"0","ActorGeo_CountryCode":country,"QuadClass":quadClass,"GoldsteinScale":0,"year":year,"month":12,"date":29,"label":1}
				dfFinal=dfFinal.append(newRowF, ignore_index=True)

print(dfFinal)
