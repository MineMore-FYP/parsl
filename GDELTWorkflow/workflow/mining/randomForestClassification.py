from parsl import load, python_app
from parsl.configs.local_threads import config
load(config)

import pandas as pd
import numpy as np
import time

import os.path
import sys
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
#ignore warnings printed on terminal
pd.options.mode.chained_assignment = None  # default='warn'

currentModule = "randomForestClassification"
workflowNumber = sys.argv[1]

if workflowNumber == "1":
	orderOfModules = userScript.orderOfModules1
	inputDataset = userScript.inputDataset1
	outputLocation = userScript.outputLocation1
elif workflowNumber == "2":
	orderOfModules = userScript.orderOfModules2
	inputDataset = userScript.inputDataset2
	outputLocation = userScript.outputLocation2


df = pd.DataFrame()
for i in range(len(orderOfModules)):
	#print(orderOfModules[i])
	if currentModule == orderOfModules[i]:
		if i == 0:
			df = pd.read_csv(inputDataset)
			break
		else:
			previousModule = orderOfModules[i-1]
			df = pd.read_csv(outputLocation + previousModule + ".csv")
			break



@python_app
def rfClassifier(estimators, dFrame):
	dataset = dFrame
	dataset.head()

	X = dataset.iloc[:, 1:5].values
	y = dataset.iloc[:, 6].values

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

	# Feature Scaling
	from sklearn.preprocessing import StandardScaler

	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)


	from sklearn.ensemble import RandomForestClassifier
	classifier = RandomForestClassifier(n_estimators=estimators, random_state=0)
	classifier.fit(X_train, y_train)
	y_pred = classifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
	#print(confusion_matrix(y_test,y_pred))
	#print(classification_report(y_test,y_pred))
	#print(accuracy_score(y_test, y_pred))
##	return str(confusion_matrix(y_test,y_pred)) + '\n' + str(classification_report(y_test,y_pred)) + '\n' + str(accuracy_score(y_test, y_pred))
	x = accuracy_score(y_test, y_pred)
	return x

results = []

for i in range(80,250,10):
	x = rfClassifier(i, df)
	#print(x)
	results.append(x)

# wait for all apps to complete
print("Job Status: {}".format([r.result() for r in results]))
