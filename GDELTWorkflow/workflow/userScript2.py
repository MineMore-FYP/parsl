import os
from collections import OrderedDict
import sys

'''
select columns
drop unique columns
drop duplicate rows
missing values mode
Add label column with value=1
replace values (Sri Lanka)

split date (y/m/d)
rename rows (to same format as GDELT)

'''

#input location
inputDataset = "/home/mpiuser/FYP/testcsv/ACLED2019-Sri_Lanka.csv"

#specify output locatiion
outputLocation = "/home/mpiuser/FYP/acled/"


'''#######################		SELECTION	####################################'''

#select columns
selectColumns = ["data_id", "event_date", "year", "country"]


'''#######################		CLEANING	####################################'''

#Drop unique columns

#drop duplicate rows
 
#mode for missing values
modeColumns = "all" 


'''#######################		TRANSFORMATION	####################################'''

#add label column 
labelValue = 1

#assign FIPS country code
country = "CE"

#split date to year, month and date


'''#######################		MERGING 	####################################'''

#generate labelled records for all days of the years
generateRecordsYears = ["2019"]

