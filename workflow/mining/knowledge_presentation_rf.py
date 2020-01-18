import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import json


currentModule = "knowledge_presentation_rf"
workflowNumber = sys.argv[1]

if workflowNumber == "1":
	orderOfModules = userScript.orderOfModules1
	#inputDataset = "/home/mpiuser/Documents/FYP/gdelt/rf.json"
	#inputDataset = "/home/amanda/FYP/gdelt/rf.json"
	outputLocation = userScript.outputLocation1
	rfAccuracyJson = outputLocation + userScript.rfAccuracyJson1
	#rfPredictFor = userScript.rfPredictFor1
	datafilesLocation = userScript.datafilesLocation
elif workflowNumber == "2":
	orderOfModules = userScript.orderOfModules2
	#inputDataset = userScript.inputDataset2
	outputLocation = userScript.outputLocation2
	rfAccuracyJson = outputLocation + userScript.rfAccuracyJson2
	#rfPredictFor = userScript.rfPredictFor2
	datafilesLocation = userScript.datafilesLocation
elif workflowNumber == "3":
	orderOfModules = userScript.orderOfModules3
	#inputDataset = "/home/mpiuser/Documents/FYP/gdelt/test.txt"
	#inputDataset = "/home/amanda/FYP/gdelt/test.txt"
	outputLocation = userScript.outputLocation3
	rfAccuracyJson = outputLocation + userScript.rfAccuracyJson3
	#rfPredictFor = userScript.rfPredictFor3
	datafilesLocation = userScript.datafilesLocation

df = pd.DataFrame()
previousModule = "normalize"
df = pd.read_csv(outputLocation + previousModule + ".csv")

#outputDataset = outputLocation + currentModule + ".csv"

#read json file
with open(rfAccuracyJson, 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)
'''
# show values
print("usd: " + str(obj['usd']))
print("eur: " + str(obj['eur']))
print("gbp: " + str(obj['gbp']))
'''

X = df.iloc[:, 1:5].values
y = df.iloc[:, 9].values

#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
sc = StandardScaler()
X = sc.fit_transform(X)
#X_test = sc.transform(X_test)


classifier = RandomForestClassifier(n_estimators=obj['estimators'], max_depth = obj['depth'], min_samples_split=obj['split'], max_features=obj['maxfeatures'], random_state=0)
classifier.fit(X, y)

#preparing test set for prediction
df_test = pd.read_csv(datafilesLocation + "test_rf.csv")
test_selected = df_test.iloc[:, 1:5].values
y_test = df_test.iloc[:, 9].values
#print(test_selected)
y_pred = classifier.predict(test_selected)

df_test['predicted_label'] = y_pred

accuracyScore = accuracy_score(y_test, y_pred)

print("Accuracy : " + str(accuracyScore))

df_test.to_csv(outputLocation + currentModule + '.csv', index = None, header=True)

print("Module Completed: Rf knowledge presentation completed")
