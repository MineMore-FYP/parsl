#categorise
import pandas as pd
import numpy as np
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import userScript

#done on integers to categorise into ranges


df = pd.read_csv(sys.argv[1])

#user defined number of categories
numberOfCategories=3

pd.cut(np.array([1, 7, 5, 4, 6, 3]), numberOfCategories)
