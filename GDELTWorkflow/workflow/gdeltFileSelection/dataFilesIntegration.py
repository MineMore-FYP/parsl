import os
import glob
import pandas as pd
from dataFileSelection import *
import csv

import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

path = userScript.datafilesLocation

#create csv header
with open(path + "CSV.header.dailyupdates.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter = "\t") # change contents to floats
    header = list(reader)[0]
    print(header)


with open(path + "combined.csv", "w", newline='', encoding='utf-8') as outcsv:
    writer = csv.writer(outcsv, delimiter=',')
    writer.writerow(header) # write the header

    
    # write the actual content line by line
    for filename in selectedFilesList:
        with open(filename, 'r', newline='', encoding='utf-8') as incsv:
            reader = csv.reader(incsv, delimiter="\t")
            writer.writerows(row + [0.0] for row in reader)


