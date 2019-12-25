import pandas as pd
from pandas import DataFrame
#from sklearn.cluster import KMeans
import numpy as np
#from sklearn.model_selection import train_test_split
#from sklearn.cluster import KMeans
#from sklearn.metrics import accuracy_score

#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages
import sys
import parsl
from parsl import load, python_app
from parsl.configs.local_threads import config

load(config)


from python1 import *

Iteration_no = sys.argv[1]
@python_app
def kmeans(n):
	import pandas as pd
	from sklearn.cluster import KMeans
	import numpy as np
	from sklearn.model_selection import train_test_split
	#from sklearn.cluster import KMeans
	from sklearn.metrics import accuracy_score


	#make this an input
	df_hist = pd.read_csv('/home/mpiuser/Documents/FYP/gdelt/missingValuesMode.csv')
	y = df_hist['QuadClass'].values
	#df_hist = df_hist['GoldsteinScale']
	#make this an input
	df_hist = df_hist[['AvgTone', 'GoldsteinScale', 'NumMentions']]
	#whats going on here?
	df_hist.to_csv('/home/mpiuser/Documents/FYP/gdelt/missingValuesMode2.csv')
	X = df_hist.values.astype(np.float)

	X_train, X_test,y_train,y_test =  train_test_split(X,y,test_size=0.20,random_state=70)
	k_means = KMeans(n_clusters=n)
	kmeans = k_means.fit(X_train)

	#print(k_means.labels_[:])
	#print(y_train[:])



	k_means.predict(X_test)

	#print(k_means.labels_[:])
	#print(y_test[:])

	score = accuracy_score(y_test,k_means.predict(X_test))
	#print('Accuracy:{0:f}'.format(score) + ' For ' + str(n) + ' clusters.\n' )


	#.reshape(-1, 1)
	#pass all the input parameters and the score
	ClusterNo_accuracy = [n,score]
	return ClusterNo_accuracy


results = []
for i in numberOfClusters:
	app_future = kmeans(i)
	results.append(app_future)

# print each job status, initially all are running
#print ("Job Status: {}".format([r.done() for r in results]))

# wait for all apps to complete
return_array = [r.result() for r in results]

dfa=pd.DataFrame(return_array)
dfa.columns = ["No_of_clusters", "Accuracy"]
#print(dfa)

dfa.to_csv (r'/home/mpiuser/Documents/FYP/gdelt/kmeans/' + Iteration_no + '_kmeans.csv', index = None, header=True)

# print each job status, they will now be finished
#print ("Job Status: {}".format(return_array))
