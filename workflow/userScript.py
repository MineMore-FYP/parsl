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
##cleaning/dropUserDefinedColumns.py
#5
##cleaning/dropColumnsCriteria.py
#6
##cleaning/dropRowsCriteria.py
#7
##cleaning/removeDuplicateRows.py
#8
##cleaning/missingValuesMode.py
#9
##transformation/normalize.py
#10
##transformation/combineColumns.py
#11
##integrateLabel/addLabelColumn.py
#12
##integrateLabel/assignCountryCode.py
#13
##integrateLabel/splitDate.py
#14
##integrateLabel/appendRecords.py
#15
##integrateLabel/integrate.py
#16
##mining/randomForestClassification.py
#17
##cleaning/dropUserDefinedColumns.py
#18
##mining/kmeansModelTraining.py
#19
##mining/knowledge_presentation.py
#20
##mining/svm.py
#21
##mining/knowledge_presentation_rf.py
#22
##mining/svm_parsl.py
#23
##mining/test_svm.py

orderOfModules1 = ["dataFilesIntegration", "countrySelection", "selectUserDefinedColumns", "dropUniqueColumns", "dropUserDefinedColumns",
"dropColumnsCriteria","dropRowsCriteria","removeDuplicateRows",
"missingValuesMode", "combineColumns", "integrate", "normalize","randomForestClassification", "knowledge_presentation_rf"]

orderOfModules2 = ["selectUserDefinedColumns","dropUniqueColumns",
"removeDuplicateRows", "missingValuesMode", "addLabelColumn",
"assignCountryCode", "splitDate", "appendRecords"]

orderOfModules3 = ["dropUserDefinedColumns","kmeansModelTraining","knowledge_presentation","svm"]

orderOfModules4 = ["svm_parsl", "test_svm"]

maxThreads = 4

'''############################File locations#################################'''
'''
When working - uncomment your location block or comments
When commiting - comment again
'''

#Gdelt FileSelection
#datafilesLocation = '/home/amanda/FYP/data/'
#datafilesLocation = '/home/clusteruser/gdeltDataFiles/'
datafilesLocation = '/home/mpiuser/Downloads/data/'


'''
#=========================AMANDA==============================
#input location
inputDataset1 = "/home/amanda/FYP/gdelt/countrySelection.csv"
inputDataset2 = "/home/amanda/FYP/testcsv/ACLED2019-Sri_Lanka.csv"
inputDataset3 = "/home/amanda/FYP/gdelt/missingValuesMode.csv"

#specify output locatiion
outputLocation1 = "/home/amanda/FYP/gdelt/"
outputLocation2 = "/home/amanda/FYP/acled/"
outputLocation3 = "/home/amanda/FYP/gdelt/"
'''

'''
#=========================CLUSTER==============================
inputDataset1 = "/home/clusteruser/FYP/gdelt/countrySelection.csv"
inputDataset2 = "/home/clusteruser/gdeltDataFiles/ACLED2019-Sri_Lanka.csv"
inputDataset3 = "/home/clusteruser/FYP/gdelt/missingValuesMode.csv"
outputLocation1 = "/home/clusteruser/FYP/gdelt/"
outputLocation2 = "/home/clusteruser/FYP/acled/"
outputLocation3 = "/home/clusteruser/FYP/gdelt/"
'''


#=======================KALPANI===============================
#input location
inputDataset1 = "/home/mpiuser/Documents/FYP/gdelt/countrySelection.csv"
inputDataset2 = "/home/mpiuser/Downloads/data/ACLED2019-Sri_Lanka.csv"
inputDataset3 = "/home/mpiuser/Documents/FYP/gdelt/integrate.csv"
inputDataset4 = "/home/mpiuser/Documents/FYP/gdelt/normalize.csv"

#specify output locatiion
outputLocation1 = "/home/mpiuser/Documents/FYP/gdelt/"
outputLocation2 = "/home/mpiuser/Documents/FYP/acled/"
outputLocation3 = "/home/mpiuser/Documents/FYP/gdelt/"
outputLocation4 = "/home/mpiuser/Documents/FYP/gdelt/"


'''
#======================RAJINI=================================
#input location
inputDataset1 = "/home/mpiuser/FYP/testcsv/dropCountry.csv"
inputDataset2 = "/home/mpiuser/FYP/testcsv/ACLED2019-Sri_Lanka.csv"

#specify output locatiion
outputLocation1 = "/home/mpiuser/FYP/gdelt/"
outputLocation2 = "/home/mpiuser/FYP/acled/"
'''

'''#############################################################################'''

#read csv to pandas df
#inputDataFrame = pd.read_csv(inputDataset)

'''#######################		SELECTION	####################################'''
#GDELT variables
#======================
startingDate = '2019.11.26'
endingDate = '2019.11.30'

#select specific country records
Actor1CountryCode = 'CE'
Actor2CountryCode = 'CE'

#select columns
#if "all" select everything. else give a list ["whatever1", "whatever2"]
selectColumns1 = ["GLOBALEVENTID","SQLDATE", "Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "QuadClass", "GoldsteinScale", "NumMentions", "AvgTone"]
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
dropCols1 = ['GLOBALEVENTID']
dropCols3 = ["ActorGeo_CountryCode", "year" , "month" , "date"]


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


#Rescale
userDefinedRescaleColumns3 = ['AvgTone']

'''#######################		MINING   	####################################'''

#mining algorithm
root1 = outputLocation1 + "rf/"
root2 = outputLocation3 + "kmeans/"

#random forest
randomForestEstimatorRange1 = [80,90]
randomForestDepthRange1 = [3,5]
randomForestSplitRange1 = [2,3]
randomForestFeaturesRange1 = [2,3]

rfAccuracyJson1 = "rf.json"
#rfPredictFor1 = [[-0.25011820853917, 5.4, 2,2]]


#k_means
numberOfClusters3 = [2,3,4,5,6,7]
clusterLabel3 = 'label'
otherInputs3 = ['AvgTone', 'GoldsteinScale', 'NumMentions', 'QuadClass']
kmeansAccuracy3 = "kmeans.json"

#svm
label3 = 'clusterNo'
value3 = [-0.25011820853917, 5.4, 2]

#svm_parsl
kernel_list4 = ['linear', 'rbf' , 'poly']
gammas4 = [10, 100]
cs4 = [0.1, 1, 10,100]
degrees4 = [1, 2, 3]


svmAccuracyJson4 = "svm.json"
