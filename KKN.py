import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
#matplotlib inline

#!wget -O teleCust1000t.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv

df = pd.read_csv('teleCust1000t.csv')
df.head()
print(df.head())
print(df['custcat'].value_counts())


df.hist(column='income', bins=50)
#plt.hist(n, 50, facecolor='blue', alpha=0.5)
plt.show()

print(df.columns)

X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
print( X[0:5] )

y = df['custcat'].values
print( y[0:5] )

X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
print ( X[0:5])
