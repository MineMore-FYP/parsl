import os
from collections import OrderedDict
import sys

#input location
inputDataset = "/home/amanda/FYP/ds/combined.csv"

'''specify output locatiion'''
outputLocation = "/home/amanda/FYP/gdelt/"

#read csv to pandas df
#inputDataFrame = pd.read_csv(inputDataset)

##select columns. if "all" select everything. else give a list ["whatever1", "whatever2"]
selectColumns = ["GLOBALEVENTID","SQLDATE", "Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "QuadClass", "GoldsteinScale", "NumMentions", "AvgTone"]
'''selectColumns = ["SQLDATE", "Actor1Geo_Type", "Actor1Geo_CountryCode","Actor2Geo_Type", "Actor2Geo_CountryCode", "QuadClass", "GoldsteinScale", "NumMentions", "AvgTone"] #done
selectColumns = ["SQLDATE"]'''

##select rows '''doesnt work'''
selectFromRow = OrderedDict()
selectFromRow['Year'] = ["2018", "2019"] 


