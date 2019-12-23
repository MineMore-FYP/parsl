import os
from collections import OrderedDict
import sys

#Workflow
#0
##gdeltFileSelection/dataFilesIntegration.py
#1
##gdeltFileSelection/countrySelection.py
#2
##selection/selectUserDefinedColumns.py
#3
##cleaning/dropUniqueColumns.py
#4
##cleaning/dropColumnsCriteria.py
#5
##cleaning/dropRowsCriteria.py
#6
##cleaning/removeDuplicateRows.py
#7
##cleaning/missingValuesMode.py
#8
##transformation/normalize.py
#9
##transformation/combineColumns.py
#10
##integrateLabel/addLabelColumn.py
#11
##integrateLabel/assignCountryCode.py
#12
##integrateLabel/splitDate.py
#13
##integrateLabel/appendRecords.py
#14
##integrateLabel/integrate.py
#15
##mining/randomForestClassification.py
#16
##cleaning/dropUserDefinedColumns.py

orderOfModules1 = ["dataFilesIntegration", "countrySelection", "selectUserDefinedColumns", "dropUniqueColumns",
"dropColumnsCriteria","dropRowsCriteria","removeDuplicateRows",
"missingValuesMode", "combineColumns", "integrate", "normalize","randomForestClassification"]

orderOfModules2 = ["selectUserDefinedColumns","dropUniqueColumns",
"removeDuplicateRows", "missingValuesMode", "addLabelColumn",
"assignCountryCode", "splitDate", "appendRecords"]

orderOfModules3 = ["dropUserDefinedColumns", "kmeans"]

#Gdelt FileSelection
datafilesLocation = '/home/amanda/FYP/data/'

#input location

inputDataset1 = "/home/amanda/FYP/testcsv/dropCountry.csv"
inputDataset2 = "/home/amanda/FYP/testcsv/ACLED2019-Sri_Lanka.csv"
inputDataset3 = "/home/amanda/FYP/gdelt/missingValuesMode.csv"
#specify output locatiion
outputLocation1 = "/home/amanda/FYP/gdelt/"
outputLocation2 = "/home/amanda/FYP/acled/"
outputLocation3 = "/home/amanda/FYP/gdelt/"

#inputDataset1 = "/home/mpiuser/FYP/testcsv/dropCountry.csv"
#inputDataset2 = "/home/mpiuser/FYP/testcsv/ACLED2019-Sri_Lanka.csv"
#inputDataset1 = "/home/mpiuser/Downloads/data/dropCountry.csv"
#inputDataset2 = "/home/mpiuser/Downloads/data/ACLED2019-Sri_Lanka.csv"

#specify output locatiion
#outputLocation1 = "/home/mpiuser/FYP/gdelt/"
#outputLocation2 = "/home/mpiuser/FYP/acled/"
#outputLocation1 = "/home/mpiuser/Documents/FYP/gdelt/"
#outputLocation2 = "/home/mpiuser/Documents/FYP/acled/"


#read csv to pandas df
#inputDataFrame = pd.read_csv(inputDataset)

'''#######################		SELECTION	####################################'''
#GDELT variables
#======================
startingDate = '2019.11.26'
endingDate = '2019.12.02'

#select specific country records
Actor1CountryCode = 'CE'
Actor2CountryCode = 'CE'

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

#drop columns
dropCols3 = ["SQLDATE", "Actor1Geo_CountryCode", "Actor2Geo_CountryCode"]


'''#######################		INTEGRATE LABEL	####################################'''


#add label column to ACLED
labelValue2 = 1

#assign FIPS country code to ACLED
country2 = "CE"

#split ACLED date to year, month and date

#generate labelled records for all days of the years
generateRecordsYears2 = ["2018", "2019"]

#merge acled records with gdelt

'''#######################		TRANSFORMATION	####################################'''

#Normalize
userDefinedNormalizeColumns1 = ["AvgTone"]

#Split into rows
#add the new column name as last element of list item
userDefinedColumsToAggregate1 = [["Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "ActorGeo_CountryCode" ]]

#encoding
userDefinedEncodeColumns = ["Actor1Geo_CountryCode"]
