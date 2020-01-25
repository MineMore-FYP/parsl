import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import sys
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import json
import pickle

currentModule = "test_svm"
workflowNumber = sys.argv[1]

if workflowNumber == "1":
	orderOfModules = userScript.orderOfModules1
	#inputDataset = "/home/mpiuser/Documents/FYP/gdelt/rf.json"
	#inputDataset = "/home/amanda/FYP/gdelt/rf.json"
	outputLocation = userScript.outputLocation1
	svmAccuracyJson = outputLocation + userScript.svmAccuracyJson1
	#rfPredictFor = userScript.rfPredictFor1
	datafilesLocation = userScript.datafilesLocation
elif workflowNumber == "2":
	orderOfModules = userScript.orderOfModules2
	#inputDataset = userScript.inputDataset2
	outputLocation = userScript.outputLocation2
	svmAccuracyJson = outputLocation + userScript.svmAccuracyJson2
	#rfPredictFor = userScript.rfPredictFor2
	datafilesLocation = userScript.datafilesLocation
elif workflowNumber == "3":
	orderOfModules = userScript.orderOfModules3
	#inputDataset = "/home/mpiuser/Documents/FYP/gdelt/test.txt"
	#inputDataset = "/home/amanda/FYP/gdelt/test.txt"
	outputLocation = userScript.outputLocation3
	svmAccuracyJson = outputLocation + userScript.svmAccuracyJson3
	#rfPredictFor = userScript.rfPredictFor3
	datafilesLocation = userScript.datafilesLocation
elif workflowNumber == "4":
	orderOfModules = userScript.orderOfModules4
	#inputDataset = "/home/mpiuser/Documents/FYP/gdelt/test.txt"
	#inputDataset = "/home/amanda/FYP/gdelt/test.txt"
	outputLocation = userScript.outputLocation4
	svmAccuracyJson = outputLocation + userScript.svmAccuracyJson4
	#rfPredictFor = userScript.rfPredictFor3
	datafilesLocation = userScript.datafilesLocation

'''
df = pd.DataFrame()
previousModule = "normalize"
df = pd.read_csv(outputLocation + previousModule + ".csv")
'''
#outputDataset = outputLocation + currentModule + ".csv"

#read json file
with open(svmAccuracyJson, 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)
'''
# show values
print("usd: " + str(obj['usd']))
print("eur: " + str(obj['eur']))
print("gbp: " + str(obj['gbp']))
'''
'''
X = df.iloc[:, 1:5].values
y = df.iloc[:, 9].values #acled label
'''

#preparing test set for prediction
df_test = pd.read_csv(datafilesLocation + "svm_test_set.csv")
X_test = df_test.iloc[:, 1:5].values
y_test = df_test.iloc[:, 9].values

'''
classifier = svm.SVC(kernel='rbf', C= obj['c'], gamma = 'auto')
classifier.fit(X, y)
'''

pkl_filename = obj['model']
# Load from file
with open(outputLocation + "picklefiles_svm/" + pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

y_pred = pickle_model.predict(X_test)

df_test['predicted_label'] = y_pred

accuracyScore = accuracy_score(y_test, y_pred)

print("Accuracy : " + str(accuracyScore))
'''
f= open(outputLocation + 'testingAccuracy/TestingAccuracySVM.txt',"w+")
f.write(str(accuracyScore))
'''

Algodict = {"Algorithm": "SVM",
"Accuracy": accuracyScore
}


with open(outputLocation + 'testingAccuracy/TestingAccuracySVM.json', 'w', encoding='utf-8') as f:
    json.dump(Algodict, f, ensure_ascii=False, indent=4)

df_test.to_csv(outputLocation + currentModule + '.csv', index = None, header=True)

print("Module Completed: SVM testing completed")
