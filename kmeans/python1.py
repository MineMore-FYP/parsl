import pandas as pd

df1 = pd.read_csv("/home/kalpani/Documents/FYP/testcsv/outputDataset.csv",engine = 'python')
header = list(df1)
numberOfClusters = [2,3,4,5,6,7]

loc = "/home/kalpani/Documents/FYP/kmeansplots"
