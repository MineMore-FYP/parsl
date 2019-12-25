import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import sys
'''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript
'''



pp = PdfPages('/home/mpiuser/Documents/FYP/gdelt/plot_Kmeans.pdf')

data = pd.read_csv('/home/mpiuser/Documents/FYP/gdelt/missingValuesMode.csv')
dfin = DataFrame(data, columns = ['AvgTone', 'GoldsteinScale', 'NumMentions'])
X = dfin.values
n = 3 #int(sys.argv[1])


kmeans = KMeans(n_clusters=n).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)

for i in range(0,n):
	
	
cluster1Centroid = centroids[0].tolist()



