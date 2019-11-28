import os
import glob
import pandas as pd
import csv
import numpy as np

#read original csv with riot information
df = pd.read_csv("/home/rajini/Desktop/riots/data.csv", header=None)
#print(df)

# parameters : the years to generate records for
years = [2018,2019]

# locations in dataframe
dfYear=df.loc[:][0]
dfMonth=df.loc[:][1]
dfDate=df.loc[:][2]
dfCountry=df.loc[:][3]

# determine unique countries; used to make seperate dataframe per country
for i in df.loc[:][3].unique():
	#print("dfCountry"+i)
	dfCountry=pd.DataFrame()
	k=0
	for j in df[:][3]:
		# query to check whether the country matches between the dataframe and row
		if j == i:
			l=df.loc[k][:]
			# matches appended to country dataframe 
			dfCountry=dfCountry.append(l)
		k=k+1
	#print(dfCountry)
	# write each country dataframe to csv file. (in seperate folder)
	dfCountry.to_csv("/home/rajini/Desktop/riots/countryDF/dfCountry"+i+".csv", sep=',', encoding='utf-8', index=False, header=False)

loc = "/home/rajini/Desktop/riots/countryDF/"

list_of_df = []

# run loop for all files in previously created dataframe folder
for f in os.listdir(loc):
	if f.endswith(".csv"):
		#print(f)
		df = pd.read_csv(loc+f,  sep = ',', header=None)
		# append dataframe to a list
		list_of_df.append(df)

#print(list_of_df[0])
#print(list_of_df[1])

'''
for df in list_of_df:
    print(df)
    print("--")
'''

ThirtyOneDays = [1,3]

for df in list_of_df:
	for y in years:
		for m in range (1,13):
			#print(m)
			if m in ThirtyOneDays:
				for d in range (1,32):
					l=pd.Series([y,m,d,"",0])
					#print(l)
					#pd.concat([df, l])
					df=df.append(l, ignore_index=True) 
			
				
			
	print(df)
'''

	
'''

	
	
			
	

df.to_csv("/home/rajini/Desktop/riots/datapp.csv", sep=',', encoding='utf-8', index=False, header=False)


'''
df.to_csv (sys.argv[1], index = False, header=True)
'''
'''
with open("/home/amanda/FYP/ds/combined.csv", "w", newline='', encoding="utf8") as outcsv:
    writer = csv.writer(outcsv, delimiter=',')
    writer.writerow(header) # write the header


    # write the actual content line by line
    for filename in selectedFiles:
        with open(filename, 'r', newline='', encoding="utf8") as incsv:
            reader = csv.reader(incsv, delimiter='\t')
            writer.writerows(row + [0.0] for row in reader)



def thirtyDayMonth():
	numberOfDays=30
	return numberOfDays

def thirtyOneDayMonth():
	numberOfDays=31

def Feb():
	numberOfDays=28

Jan=thirtyOneDayMonth()
Feb=Feb()
March=thirtyOneDayMonth()
April=thirtyDayMonth()
May=thirtyOneDayMonth()
June=thirtyDayMonth()
July=thirtyOneDayMonth()
Aug=thirtyOneDayMonth
Sep=thirtyDayMonth()
Oct=thirtyOneDayMonth()
Nov=thirtyDayMonth()
Dec=thirtyOneDayMonth()
'''
