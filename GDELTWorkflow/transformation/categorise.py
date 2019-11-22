#categorise
import pandas as pd
import numpy as np

import parsl
from parsl import load, python_app
from parsl.configs.local_threads import config

load(config)

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

#done on integers to categorise into ranges


df = pd.read_csv("/home/kalpani/Documents/FYP/testcsv/test.csv")

@python_app
def categorize():
	#user defined number of categories
	numberOfCategories=3

	pd.cut(np.array([1, 7, 5, 4, 6, 3]), numberOfCategories)

categorize()
