
print("DecisionTree")

import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#wget -O drug200.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv


my_data = pd.read_csv("drug200.csv", delimiter=",")
my_data[0:5]