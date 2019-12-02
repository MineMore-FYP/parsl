#Select GDELT data files for processing 
#Files in the format 20180720.CSV 

#future work : Train review of file name to direct to suitable file selection functions

import os
import glob

#Kalpani
#path = 'D:/FYP/ds'

#Amanda
path = '/home/amanda/FYP/ds'
os.chdir(path)

allFiles = os.listdir(path)

##File selection

selectedFiles = []

#select data files for a given month
def getMonthlyFiles(m):
    if (m == "JANUARY"):
        selectMonth = "01"
    elif (m == "FEBRUARY"):
        selectMonth = "02"
    elif (m == "MARCH"):
        selectMonth = "03"
    elif (m == "APRIL"):
        selectMonth = "04"
    elif (m == "MAY"):
        selectMonth = "05"
    elif (m == "JUNE"):
        selectMonth = "06"
    elif (m == "JULY"):
        selectMonth = "07"
    elif (m == "AUGUST"):
        selectMonth = "08"
    elif (m == "SEPTEMBER"):
        selectMonth = "09"
    elif (m == "OCTOBER"):
        selectMonth = "10"
    elif (m == "NOVEMBER"):
        selectMonth = "11"
    elif (m == "DECEMBER"):
        selectMonth = "12"
    return selectMonth

#def getAnnualFiles(m):

#def getDateRangeFiles(m):
            
#def getDayOfTheWeekFiles(m):

#userdefined month- input from swift script
userMonth = "JULY"

#for all files in directory select files with matching int of user defined month
for filename in allFiles:
    #print(filename)
    desiredMonth = getMonthlyFiles(userMonth)
    #print(desiredMonth)
    filenameMonth=filename[4:6]
    #print(filenameMonth)
    #print(filenameMonth == desiredMonth)
    if filenameMonth == desiredMonth:
        selectedFiles.append(filename)

print(selectedFiles)