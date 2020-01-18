# importing necessary libraries 
#from sklearn import datasets 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split 
import pandas as pd
import numpy as np
import sys

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript


currentModule = "svm"
workflowNumber = sys.argv[1]
#Iteration_no = sys.argv[2]

if workflowNumber == "1":
	orderOfModules = userScript.orderOfModules1
	inputDataset = userScript.inputDataset1
	outputLocation = userScript.outputLocation1
	clusterLabel = userScript.clusterLabel1
	otherInputs = userScript.otherInputs1
	numberOfClusters=userScript.numberOfClusters1
elif workflowNumber == "2":
	orderOfModules = userScript.orderOfModules2
	inputDataset = userScript.inputDataset2
	outputLocation = userScript.outputLocation2
	clusterLabel = userScript.clusterLabel3
	otherInputs = userScript.otherInputs3
	numberOfClusters = userScript.numberOfClusters2
elif workflowNumber == "3":
	orderOfModules = userScript.orderOfModules3
	inputDataset = userScript.inputDataset3
	outputLocation = userScript.outputLocation3
	clusterLabel = userScript.clusterLabel3
	otherInputs = userScript.otherInputs3
	numberOfClusters = userScript.numberOfClusters3
	label = userScript.label3
	value= userScript.value3

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


#outputDataset = outputLocation + currentModule + ".csv"
#df = pd.read_csv('/home/mpiuser/Documents/FYP/gdelt/labeledKmeansOutput.csv')


# X -> features, y -> label 
y = df[label].values
df = df[otherInputs]
X = df.values


# dividing X, y into train and test data 
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 

# training a linear SVM classifier 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X, y) 


#preparing test set for prediction
df_test = pd.read_csv(datafilesLocation + "test_kmeans.csv")
test_selected = df_test.iloc[:, 1:5].values
y_test = df_test.iloc[:, 9].values
#print(test_selected)
y_pred = classifier.predict(test_selected)

df_test['predicted_label'] = y_pred

accuracyScore = accuracy_score(y_test, y_pred)

print("Accuracy : " + str(accuracyScore))

svm_predictions = svm_model_linear.predict([value])
print(svm_predictions) 

# creating a confusion matrix 
#cm = confusion_matrix(y_test, svm_predictions) 
print("Module Completed: SVM classification completed")
