import os
import glob
import pandas as pd
from dataFileSelection import *
import csv

#create csv header
with open("/home/amanda/FYP/ds/CSV.header.dailyupdates.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter = "\t") # change contents to floats
    header = list(reader)[0]
    print(header)


with open("/home/amanda/FYP/ds/combined.csv", "w", newline='', encoding="utf8") as outcsv:
    writer = csv.writer(outcsv, delimiter=',')
    writer.writerow(header) # write the header


    # write the actual content line by line
    for filename in selectedFiles:
        with open(filename, 'r', newline='', encoding="utf8") as incsv:
            reader = csv.reader(incsv, delimiter='\t')
            writer.writerows(row + [0.0] for row in reader)
