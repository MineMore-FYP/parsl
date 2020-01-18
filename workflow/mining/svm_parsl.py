from parsl import load, python_app

import pandas as pd
import numpy as np
import time

import os.path
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
import parslConfig
#ignore warnings printed on terminal
pd.options.mode.chained_assignment = None  # default='warn'

currentModule = "svm_parsl"
workflowNumber = sys.argv[1]
#Iteration_no = sys.argv[2]

if workflowNumber == "1":
	orderOfModules = userScript.orderOfModules1
	inputDataset = userScript.inputDataset1
	outputLocation = userScript.outputLocation1
	kernel_list = userScript.kernel_list1
	
elif workflowNumber == "2":
	orderOfModules = userScript.orderOfModules2
	inputDataset = userScript.inputDataset2
	outputLocation = userScript.outputLocation2
	kernel_list = userScript.kernel_list2
elif workflowNumber == '3':
	orderOfModules = userScript.orderOfModules3
	inputDataset = userScript.inputDataset3
	outputLocation = userScript.outputLocation3
	kernel_list = userScript.kernel_list3
elif workflowNumber == '4':
	orderOfModules = userScript.orderOfModules4
	inputDataset = userScript.inputDataset4
	outputLocation = userScript.outputLocation4
	kernel_list = userScript.kernel_list4
	cs = userScript.cs4
	gammas = userScript.gammas4
	degrees = userScript.degrees4

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

#outputLocation = outputLocation + "svm/"

@python_app
def svmClassifier(c, dFrame):
	dataset = dFrame
	dataset.head()

	X = dataset.iloc[:, 1:5].values
	y = dataset.iloc[:, 9].values

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=109)

	# Feature Scaling
	#from sklearn.preprocessing import StandardScaler

	#sc = StandardScaler()
	#X_train = sc.fit_transform(X_train)
	#X_test = sc.transform(X_test)


	from sklearn import svm
	classifier = svm.SVC(kernel='rbf', C= c)
	classifier.fit(X_train, y_train)
	y_pred = classifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
	#print(confusion_matrix(y_test,y_pred))
	#print(classification_report(y_test,y_pred))
	#print(accuracy_score(y_test, y_pred))
##	return str(confusion_matrix(y_test,y_pred)) + '\n' + str(classification_report(y_test,y_pred)) + '\n' + str(accuracy_score(y_test, y_pred))
	accuracyScore = accuracy_score(y_test, y_pred)
	retArray = [c, accuracyScore]
	return retArray

results = []


for i in cs:
	x = svmClassifier(i,df)
	results.append(x)


# wait for all apps to complete
return_array = [r.result() for r in results]

dfa = pd.DataFrame(return_array)
dfa.columns = ["C", "Accuracy"]
#print(dfa)

dfa.to_csv (outputLocation + 'svm.csv', index = None, header=True)
print("SVM model selection module completed.\n")

# wait for all apps to complete
#print("Job Status: {}".format([r.result() for r in results]))
