import pandas as pd
from pandas import DataFrame
from sklearn.cluster import KMeans
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import parsl
from parsl import load, python_app
from parsl.configs.local_threads import config

load(config)


from python1 import *
from python2 import *


@python_app
def kmeans(n):	
	for i in header:
		for j in header:
			if(i != j):
				dfin = DataFrame(df1,columns=[i,j])
				X = dfin.values
				kmeans = KMeans(n_clusters=n).fit(X)
				centroids = kmeans.cluster_centers_
				print("x axis: "+i + " , y axis: " + j)
				print(centroids)
				print("\n")
				
	strng = 'kmeans done for ' + str(n) + ' clusters'
	return strng			    						  			    	
					    						    	

results = []
for i in numberOfClusters:
	app_future = kmeans(i)
	results.append(app_future)
	
# print each job status, initially all are running
print ("Job Status: {}".format([r.done() for r in results]))

# wait for all apps to complete
[r.result() for r in results]

# print each job status, they will now be finished
print ("Job Status: {}".format([r.result() for r in results]))
