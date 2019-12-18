import os
from collections import OrderedDict
import sys

'''
select columns
drop duplicate rows
drop unique columns
missing values mode
split date (y/m/d)
rename rows (to same format as GDELT)
replace values (Sri Lanka)
Add label column with value=1
'''

#input location
inputDataset = "/home/rajini/FYP/testcsv/ACLED2019-Sri_Lanka.csv"

#specify output locatiion
outputLocation = "/home/rajini/FYP/acled/"


'''#######################		SELECTION	####################################'''

#select columns
selectColumns = ["data_id", "event_date", "year", "country"]


'''#######################		CLEANING	####################################'''

#drop duplicate rows

#Drop unique columns
 
#mode for missing values
modeColumns = "all" 


'''#######################		TRANSFORMATION	####################################'''

#Normalize
userDefinedNormalizeColumns = ["AvgTone"]

#Split into rows
#add the new column name as last element of list item
userDefinedColumsToAggregate = [["Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "ActorGeo_CountryCode" ]]


#encoding
userDefinedEncodeColumns = ["Actor1Geo_CountryCode"]
