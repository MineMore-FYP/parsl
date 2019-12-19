import os
from collections import OrderedDict
import sys


#Workflow

##selection/selectUserDefinedColumns.py
##cleaning/dropUniqueColumns.py
##cleaning/dropColumnsCriteria.py
##cleaning/dropRowsCriteria.py
##cleaning/removeDuplicateRows.py
##cleaning/missingValuesMode.py
#transformation/normalize.py
##transformation/splitIntoRows.py

orderOfModules = ["selectUserDefinedColumns", "dropUniqueColumns",
"dropColumnsCriteria","dropRowsCriteria","removeDuplicateRows",
"missingValuesMode", "splitIntoRows"]

#input location

inputDataset1 = "/home/amanda/FYP/testcsv/dropCountry.csv"


#specify output locatiion
outputLocation1 = "/home/amanda/FYP/gdelt/"
#outputLocation = "/home/mpiuser/FYP/gdelt/"


#GDELT variables
#======================
startingDate = '2019.11.26'
endingDate = '2019.12.02'

datafilesLocation = '/home/mpiuser/Downloads/data/'
#select specific country records
Actor1CountryCode = 'LKA'
Actor2CountryCode = 'LKA'

#read csv to pandas df
#inputDataFrame = pd.read_csv(inputDataset)

'''#######################		SELECTION	####################################'''

#select columns
#if "all" select everything. else give a list ["whatever1", "whatever2"]
selectColumns1 = ["GLOBALEVENTID","SQLDATE", "Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "Actor1EthnicCode", "Actor2EthnicCode", "QuadClass", "GoldsteinScale", "NumMentions", "AvgTone"]
selectColumns2 = ["fssfjfn"]
#select rows
#selectFromRow = OrderedDict()
#selectFromRow['Year'] = ["2018", "2019"] #doesnt work


'''#######################		CLEANING	####################################'''

#Run anyway - Drop unique columns

#user defined missing values
missingValues = ["n/a", "na", "--"]

#drop columns according to user defined empty value percentage
userDefinedColPercentage1 = 50

#drop rows according to user defined empty value percentage. if 85.71% isnt empty, keep
userDefinedRowPercentage1 = 85.71

#drop duplicate rows - run anyway

#Research how best to fill missing values
#mode for user defined columns
modeColumns1 = "all"


'''#######################		TRANSFORMATION	####################################'''

#Normalize
userDefinedNormalizeColumns1 = ["AvgTone"]

#Split into rows
#add the new column name as last element of list item
userDefinedColumsToAggregate1 = [["Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "ActorGeo_CountryCode" ]]

#encoding
userDefinedEncodeColumns = ["Actor1Geo_CountryCode"]
