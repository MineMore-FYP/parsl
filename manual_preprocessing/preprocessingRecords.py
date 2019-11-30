import os
import glob
import pandas as pd
import csv
import numpy as np

#read original csv with riot information
df = pd.read_csv("/home/rajini/Desktop/riots/data.csv", header=None)

# parameters : the years to generate records for
years = [2018,2019]

# locations in dataframe
dfYear=df.loc[:][0]
dfMonth=df.loc[:][1]
dfDate=df.loc[:][2]
dfCountry=df.loc[:][3]


# SEPERATE DATAFRAMES BY COUNTRY

# determine unique countries; used to make seperate dataframe per country
for i in df.loc[:][3].unique():
	dfCountry=pd.DataFrame()
	k=0
	for j in df[:][3]:
		# query to check whether the country matches between the dataframe and row
		if j == i:
			l=df.loc[k][:]
			# matches appended to country dataframe 
			dfCountry=dfCountry.append(l)
		k=k+1
	# write each country dataframe to csv file. (in seperate folder)
	dfCountry.to_csv("/home/rajini/Desktop/riots/countryDF/dfCountry"+i+".csv", sep=',', encoding='utf-8', index=False, header=False)


# INSERT NEW RECORD FOR EVERY DAY IN THE YEAR

loc = "/home/rajini/Desktop/riots/countryDF/"

list_of_df = []

# run loop for all files in previously created dataframe folder
for f in os.listdir(loc):
	if f.endswith(".csv"):
		df = pd.read_csv(loc+f,  sep = ',', header=None)
		# append dataframe to a list
		list_of_df.append(df)

ThirtyDays = [4,6,9,11]
ThirtyOneDays = [1,3,5,7,8,10,12]
TwentyEightDays = [2]

# create records with zero values for unrest for all days, months and years
for df in list_of_df:	
	# get country name for dataframe from the first row of df 		
	countryName = df.loc[0][3]
	for y in years:
		for m in range (1,13):
			#print(m)
			if m in ThirtyOneDays:
				for d in range (1,32):
					l=pd.Series([y,m,d,countryName,0])
					df=df.append(l, ignore_index=True) 

			if m in ThirtyDays:
				for d in range (1,31):
					l=pd.Series([y,m,d,countryName,0])
					df=df.append(l, ignore_index=True) 

			if m in TwentyEightDays:
				for d in range (1,29):
					l=pd.Series([y,m,d,countryName,0])
					df=df.append(l, ignore_index=True) 

	df.to_csv("/home/rajini/Desktop/riots/filledDF/dfFilledCountry"+countryName+".csv", sep=',', encoding='utf-8', index=False, header=False)


# REMOVE DUPLICATE ROWS 

loc2 = "/home/rajini/Desktop/riots/filledDF/"

list_of_filled_df = []

# run loop for all files in previously created dataframe folder
for f in os.listdir(loc2):
	if f.endswith(".csv"):
		df = pd.read_csv(loc2+f,  sep = ',', header=None)
		# append dataframe to a list
		list_of_filled_df.append(df)

# handle duplicate zero records
for df in list_of_filled_df:
	# get country name for dataframe from the first row of df 		
	countryName = df.loc[0][3]

	# Select all duplicate rows based on multiple columns
	# leave the first record (showing riot) and delete the next
	# For the subset argument, specify the first n-1 columns
	df = df.drop_duplicates(subset=df.columns[:-1], keep='first')	
	df.to_csv("/home/rajini/Desktop/riots/removeDuplicateDF/dfRemoveDuplicate"+countryName+".csv", sep=',', encoding='utf-8', index=False, header=False)


# COMBINE ALL DATAFRAMES

loc4 = "/home/rajini/Desktop/riots/removeDuplicateDF/"
os.chdir(loc4)

allFiles = os.listdir(loc4)

# CSV file selection

selectedFiles = []

for filename in allFiles:
    	selectedFiles.append(filename)

# Create new CSV file to write all CSV files generated from previous step 
with open("/home/rajini/Desktop/riots/combinedRiots.csv", "w", newline='', encoding="utf8") as outcsv:
	writer = csv.writer(outcsv, delimiter=',')

	# write the header
	writer.writerow(["Year", "Month", "Date", "ActorGeo_CountryCode", "Indicator"]) 
	
	# write the actual content line by line
	for filename in selectedFiles:
		with open(filename, 'r', newline='', encoding="utf8") as incsv:
			reader = csv.reader(incsv, delimiter=',')
			writer.writerows(row for row in reader)

'''
# CONCATENATE COLUMNS TO GET SQL DATE

loc3 = "/home/rajini/Desktop/riots/removeDuplicateDF/"

list_of_duplicate_removed_df = []

# run loop for all files in previously created dataframe folder
for f in os.listdir(loc3):
	if f.endswith(".csv"):
		#print(f)
		df = pd.read_csv(loc3+f,  sep = ',', header=None)
		# append dataframe to a list
		list_of_duplicate_removed_df.append(df)
		#print(list_of_filled_df)

for df in list_of_duplicate_removed_df:
	# get country name for dataframe from the first row of df 		
	countryName = df.loc[0][3]

	# convert float to int	
	for i in range (3):
		df[i]=df[i].astype(int)
	#print(df.dtypes)

	# convert int to string
	for i in range (3):
		df[i]=df[i].astype(str)

		count=0

		# add "0" in front of one digit months and dates (in order to derive proper SQL date)
		for j in df.loc[:][i]:
			if j in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
				j=j.zfill(2)
				#print(j)
				df.set_value([count], [i], j)
			count=count+1
	#print(df.dtypes)
	
	# obtain SQLDATE in column 1
	df[0] = df[0]+df[1]+df[2]

	# drop month and date columns
	df = df.drop([1, 2], axis=1)

	#df.columns = ['SQLDATE', 'ActorGeo_CountryCode', 'Indicator']

	#print(df)
	
	df.to_csv("/home/rajini/Desktop/riots/sqldateDF/dfsqldate"+countryName+".csv", sep=',', encoding='utf-8', index=False, header=False)

'''
