# importing necessary libraries 
#from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
import pandas as pd
import numpy as np


df = pd.read_csv('/home/mpiuser/Documents/FYP/gdelt/labeledKmeansOutput.csv')


# X -> features, y -> label 
y = df['clusterNo'].values
#df_hist = df_hist['GoldsteinScale']
#make this an input
df = df[['AvgTone', 'GoldsteinScale', 'NumMentions']]
X = df.values


# dividing X, y into train and test data 
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 

# training a linear SVM classifier 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X, y) 


# model accuracy for X 
accuracy = svm_model_linear.score(X, y) 
print(accuracy)

svm_predictions = svm_model_linear.predict([[-0.25011820853917, 5.4, 2]])
print(svm_predictions) 

# creating a confusion matrix 
#cm = confusion_matrix(y_test, svm_predictions) 

