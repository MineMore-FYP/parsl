import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import sys

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import json

currentModule = "knowledge_presentation"
workflowNumber = sys.argv[1]

if workflowNumber == "1":
	orderOfModules = userScript.orderOfModules1
	inputDataset = userScript.inputDataset1
	outputLocation = userScript.outputLocation1
	kmeansAccuracy = outputLocation + userScript.kmeansAccuracy1
	datafilesLocation = userScript.datafilesLocation
elif workflowNumber == "2":
	orderOfModules = userScript.orderOfModules2
	inputDataset = userScript.inputDataset2
	outputLocation = userScript.outputLocation2
	kmeansAccuracy = outputLocation + userScript.kmeansAccuracy2
	datafilesLocation = userScript.datafilesLocation
elif workflowNumber == "3":
	orderOfModules = userScript.orderOfModules3
	#inputDataset = "/home/mpiuser/Documents/FYP/gdelt/kmeans.txt"
	#inputDataset = "/home/amanda/FYP/gdelt/kmeans.txt"
	outputLocation = userScript.outputLocation3
	kmeansAccuracy = outputLocation + userScript.kmeansAccuracy3
	datafilesLocation = userScript.datafilesLocation

df = pd.DataFrame()
previousModule = "dropUserDefinedColumns"
df = pd.read_csv(outputLocation + previousModule + ".csv")


outputDataset = outputLocation + currentModule + ".csv"


#data = pd.read_csv('/home/mpiuser/Documents/FYP/gdelt/missingValuesMode.csv')
dfin = DataFrame(df, columns = ['AvgTone', 'GoldsteinScale', 'NumMentions', 'QuadClass'])
X = dfin.values
y = df['label']


#read json
f= open(kmeansAccuracy, "r")
n = int(f.read()) #int(sys.argv[1])


#preparing test set for prediction
df_test = pd.read_csv(datafilesLocation + "kmeans_test_set.csv")
X_test = DataFrame(df_test, columns = ['AvgTone', 'GoldsteinScale', 'NumMentions', 'QuadClass']).values
y_test = df_test['label'].values

kmeans = KMeans(n_clusters=n, random_state= 0).fit(X)
#dfin['clusterNo'] = kmeans.labels_[:]
#centroids = kmeans.cluster_centers_


#print(test_selected)
y_pred = kmeans.predict(X_test)

df_test['predicted_label'] = y_pred

accuracyScore = accuracy_score(y_test, y_pred)

print("Accuracy : " + str(accuracyScore))
'''
f= open(outputLocation + 'testingAccuracy/TestingAccuracyKmeans.txt',"w+")
f.write(str(accuracyScore))
'''

Algodict = {"Algorithm": "Kmeans",
"Accuracy": accuracyScore
}


with open(outputLocation + 'testingAccuracy/TestingAccuracyKmeans.json', 'w', encoding='utf-8') as f:
    json.dump(Algodict, f, ensure_ascii=False, indent=4)

#df_test['SQLDATE'] = df['SQLDATE']

df_test.to_csv (outputDataset, index = None, header=True)
print("Module Completed: Kmeans testing")

'''
#print(np.unique(kmeans.labels_[:]))
u = kmeans.labels_[:]
zeros = np.sum(u == 0)
ones = np.sum(u == 1)
#print(zeros)
#print(ones)

centroids = kmeans.cluster_centers_
#print(centroids)
#print(dfin)
'''
