# -*- coding: utf-8 -*-
"""wines.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qsT-aoe-_u0ieWjz6VVaw8L-lcklUhtB
"""

!wget https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names

#@title Load Modules
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# load method for splitting data
from sklearn.model_selection import train_test_split

# logistics regression
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
white=pd.read_csv('winequality-white.csv',sep=';')
white.head().shape

with open('/content/winequality.names',mode='r') as txt:
  text_data=txt.read()
print(text_data)

#red=pd.read_csv('winequality-red.csv.1',sep=';')#sep for separete

#red.info()

white.info()

white.describe().loc[['mean','std']]

#red.describe().loc[['mean','std']]

#np.allclose(red.describe().loc[['mean','std']],white.describe().loc[['mean','std']])

white['quality'].value_counts()
white.corr()

# load method for splitting data
from sklearn.model_selection import train_test_split

# make split (dataframe and series) (can also use numpy array)
Xtrain,Xtest,ytrain,ytest=train_test_split(white.iloc[:,:-1],white['quality'],
                                           test_size=0.33)
# see shape of data (daatframes and series)
Xtrain.shape,ytrain.shape,Xtest.shape,ytest.shape

best=LinearRegression()
best.fit(Xtrain,ytrain)  #best case

# regress=LinearRegression()
# make model train (fit) (calculated m and c (feature extraction))
print('R2 Score (training): ',best.score(Xtrain,ytrain))
print('R2 Score (testing): ',best.score(Xtest,ytest))

