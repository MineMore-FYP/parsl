import os
from collections import OrderedDict
import sys

#Workflow

##selection/selectUserDefinedColumns.py
##cleaning/dropUniqueColumns.py
##cleaning/dropColumnsCriteria.py
##cleaning/dropRowsCriteria.py
##cleaning/removeDuplicateRows.py
##transformation3/splitIntoRows.py
##transformation3/countrySelection.py

##cleaning/missingValuesMode.py
#transformation/normalize.py
##transformation/splitIntoRows.py

orderOfModules = ["splitIntoRows", "countrySelection"]

#input location
inputDataset = "/home/mpiuser/FYP/testcsv/removeDuplicateRows.csv"

#specify output locatiion
outputLocation = "/home/mpiuser/FYP/kmeans/"

#split into rows based on actor1 and actor2 Geo country codes

#select rows for below country only
ActorGeo_CountryCode = "CE"



