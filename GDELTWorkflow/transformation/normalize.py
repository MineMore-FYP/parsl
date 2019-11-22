# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
import pandas
import numpy
import scipy

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
dataframe = pandas.read_csv(url)

array = dataframe.values

scaler = Normalizer().fit(array)
normalized = scaler.transform(array)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(normalized[0:5,:])

#last two lines for printing first six rows. change as required to output CSV.