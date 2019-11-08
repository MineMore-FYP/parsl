import os
from collections import OrderedDict
import sys

#Workflow

#input   location

#inputDataset = "/home/rajini/FYP/testcsv/test.csv"
inputDataset = "/home/amanda/FYP/testcsv/test.csv"

#specify output locatiion
#outputDataset = "/home/rajini/FYP/testcsv/outputDataset.csv"
outputDataset = "/home/amanda/FYP/testcsv/out.csv"

#wait time between each step of workflow (in milli seconds)
waitTime = 10000

#SELECTION
#select columns
#if "all" select everything. else give a list ["whatever1", "whatever2"]
selectColumns = ["GLOBALEVENTID","SQLDATE", "Year", "Actor2Code", "Actor2Name", "Actor2Religion1Code", "Actor2Type1Code", "EventCode", "EventRootCode", "QuadClass", "GoldsteinScale", "NumMentions", "NumSources", "NumArticles", "AvgTone", "Actor2Geo_FullName", "SOURCEURL"]

#select rows
selectFromRow = OrderedDict()
selectFromRow['Year'] = ["2018", "2019"]
selectFromRow['Actor1Name'] = ["DUTCH"]

#CLEANING
#Drop unique columns
#Drop one value columns

#user defined missing values
missingValues = ["n/a", "na", "--"]

#Drop user defined cols
#user defined column array
dropColumns = ["SQLDATE", "SOURCEURL"]

#drop columns according to user defined empty value percentage
userDefinedColPercentage = 30

#drop user defined rows
dropFromRow = OrderedDict()
dropFromRow['Actor2Name'] = ["LONDON", "DUTCH"]
dropFromRow['EventCode'] = ["40"]

#drop rows according to user defined empty value percentage
userDefinedRowPercentage = 20

#remove duplicate rows

#missing value interpolation
#all int and float columns interpolated
interpolateColumns = "all" #if interpolateColumns = "all", all int columns, else give a list

#mode for user defined columns
#all the rest left from interpolate, mode
modeColumns = "all"

#fill missing value with a constant
#missingValueCons = OrderedDict()
#missingValueCons["PID"] = [100045]
#missingValueCons["SQ_FT"] = 1000

#transformation
#Standardize
userDefinedStandardizeColumns = ["AvgTone"] #standadizeColumns = "all", all int columns, else give a list

#rescale
userDefinedRescaleColumns = OrderedDict()
#0 = lowerBoundry, 100 = upperBoundry
userDefinedRescaleColumns["NumMentions"] = [0, 100]
userDefinedRescaleColumns["NumSources"] = [0, 100]
userDefinedRescaleColumns["NumArticles"] = [0, 100]

#binarize
userDefinedBinarizeColumns = OrderedDict()
#0 = lowerBoundry, 100 = upperBoundry
userDefinedBinarizeColumns["NumMentions"] = [10.0]
userDefinedBinarizeColumns["NumSources"] = [10.0]
userDefinedBinarizeColumns["NumArticles"] = [10.0]


#encoding - gives an automatical numerical value to string categorical columns
userDefinedEncodeColumns = ["Actor2Code", "Actor2Name", "Actor2Geo_FullName"]

#Binning
#userDefinedBinningColumns = OrderedDict()
#10 = number of bins
#userDefinedBinningColumns["AvgTone"] = [10]


#mining
#which algorithms to use. and relevant params

#kmeans
#selectedColumns1 = selectColumns - dropColumns
numberOfClusters = 3

startWithNumberOfClusters = 2
endWithNumberOfClusters = 8
#input   location
plotLocation = "/home/amanda/FYP/testcsv"


#KNN
#define targetColumn
targetColumnName = "QuadClass"
targetColumn = ["QuadClass"]
numberOfneighbours = 5

#linear regression
#selectedColumns2 = selectColumns - dropColumns

#knowledge presentation
