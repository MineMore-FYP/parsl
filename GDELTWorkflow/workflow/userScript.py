import os
from collections import OrderedDict
import sys


#Workflow
#0
##selection/selectUserDefinedColumns.py
#1
##cleaning/dropUniqueColumns.py
#2
##cleaning/dropColumnsCriteria.py
#3
##cleaning/dropRowsCriteria.py
#4
##cleaning/removeDuplicateRows.py
#5
##cleaning/missingValuesMode.py
#6
##transformation/normalize.py
#7
##transformation/splitIntoRows.py


orderOfModules1 = ["selectUserDefinedColumns", "dropUniqueColumns",
"dropColumnsCriteria","dropRowsCriteria","removeDuplicateRows",
"missingValuesMode", "splitIntoRows"]

orderOfModules2 = ["selectUserDefinedColumns","dropUniqueColumns", "removeDuplicateRows",
"missingValuesMode"]

#input location

inputDataset1 = "/home/mpiuser/Downloads/data/dropCountry.csv"
inputDataset2 = "/home/mpiuser/Documents/FYP/ACLED2019-Sri_Lanka.csv"

#specify output locatiion
outputLocation1 = "/home/mpiuser/Documents/FYP/gdelt/"
outputLocation2 = "/home/mpiuser/FYP/acled/"
#outputLocation = "/home/mpiuser/FYP/gdelt/"


#GDELT variables
#======================
startingDate = '2019.11.26'
endingDate = '2019.12.02'

datafilesLocation = '/home/mpiuser/Downloads/data/'
#select specific country records
Actor1CountryCode = 'CE'
Actor2CountryCode = 'CE'

#read csv to pandas df
#inputDataFrame = pd.read_csv(inputDataset)

'''#######################		SELECTION	####################################'''

#select columns
#if "all" select everything. else give a list ["whatever1", "whatever2"]
selectColumns1 = ["GLOBALEVENTID","SQLDATE", "Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "Actor1EthnicCode", "Actor2EthnicCode", "QuadClass", "GoldsteinScale", "NumMentions", "AvgTone"]
selectColumns2 = ["data_id", "event_date", "year", "country"]

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
modeColumns2 = "all"


'''#######################		TRANSFORMATION	####################################'''

#Normalize
userDefinedNormalizeColumns1 = ["AvgTone"]

#Split into rows
#add the new column name as last element of list item
userDefinedColumsToAggregate1 = [["Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "ActorGeo_CountryCode" ]]

#encoding
userDefinedEncodeColumns = ["Actor1Geo_CountryCode"]
