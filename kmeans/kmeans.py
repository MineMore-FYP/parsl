import pandas as pd
from parsl import load, python_app
from parsl.configs.local_threads import config
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
load(config)


from python1 import *
from python2 import *


@python_app
def kmeans(n):
	
	clusters = str(n)
	
	pp = PdfPages(loc + '/plot_Kmeans_' + clusters + '.pdf')
	
	dfin = DataFrame(df1,columns=["GoldsteinScale","AvgTone"])
	X = dfin.values
	#kmeans = KMeans(n_clusters=userScript.numberOfClusters).fit(X)
	kmeans = KMeans(n_clusters=n).fit(X)
	centroids = kmeans.cluster_centers_
	#print("x axis: "+i + " , y axis: " + j)
	#print(centroids)
	#print("\n")						    					    	
	plt.scatter(X[:,0], X[:,1], c= kmeans.labels_, cmap='rainbow')
	plt.xlabel("GoldsteinScale")
	plt.ylabel("AvgTone")
	plt.scatter(centroids[:, 0], centroids[:, 1], c='black')
	plt.savefig(pp, format='pdf')
	plt.close()
	pp.close()
	return centroids					    						  			    	
					    						    	
	

#df1 = fun_df()

#print(df1.result())
df1 = pd.read_csv("/home/kalpani/Documents/FYP/testcsv/outputDataset.csv",engine = 'python')
#print(df1)
header = list(df1)
#print(list(df1))
loc = plotLocation

results = []
for i in numberOfClusters:
	centroids1 = kmeans(i)
	print(i)
	results.append(centroids1)
	

print(results)


#df_final = app_dropColumns(dropCols)
#print(df_final.result())
