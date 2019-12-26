import pandas as pd
import csv
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import sys

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript




#pp = PdfPages('/home/mpiuser/Documents/FYP/gdelt/plot_Kmeans.pdf')

data = pd.read_csv('/home/mpiuser/Documents/FYP/gdelt/missingValuesMode.csv')
dfin = DataFrame(data, columns = ['AvgTone', 'GoldsteinScale', 'NumMentions'])
X = dfin.values

n = 2 #int(sys.argv[1])


kmeans = KMeans(n_clusters=n, random_state= 0).fit(X)
dfin['clusterNo'] = kmeans.labels_[:]
print(np.unique(kmeans.labels_[:]))
u = kmeans.labels_[:]
zeros = np.sum(u == 0)
ones = np.sum(u == 1)
print(zeros)
print(ones)
centroids = kmeans.cluster_centers_
print(centroids)
#print(dfin)

dfin.to_csv (userScript.outputLocation3 + 'kmeans/' + 'labeledKmeansOutput.csv', index = None, header=True)



