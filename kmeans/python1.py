import pandas as pd

def add():
	return random.randint(1,101)+ random.randint(1,101)


x = 1

df = pd.read_csv("/home/kalpani/Documents/FYP/testcsv/test1.csv")

dropCols = ["age", "height"]

numberOfClusters = [2,3,4,5,6,7]



plotLocation = "/home/kalpani/Documents/FYP"
