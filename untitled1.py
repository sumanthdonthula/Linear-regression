# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:03:00 2019

@author: SUMANTH
"""
"""In this code we will find the number of trees required to co operate carbondioxide data in India by using
the data from The worldbank(idrb,ida)"""

#linear regression
import numpy as np#importing numpy which performs numerical operations
import pandas as pd#importing pandas which reads the set of data

from matplotlib import pyplot as plt #matplot library used for plotting
from sklearn.linear_model import LinearRegression #importing linear regreesion from skikit learn

df=pd.read_csv('dat.csv') #importing data

Lr=LinearRegression() #calling linear regression
Lr.fit(train_x, train_y)#fitting the linear regression model for the given data

train_y=df['emission'].values[:,np.newaxis]#features of y

train_x=df['year'].values[:,np.newaxis]#features of x which starts form the year 1960 to 2014
 




test=pd.read_csv('testing.csv')#The data tested from years 2015 to 2025

pre=Lr.predict(test) #predict command for preddiction
plt.scatter(train_x,train_y,color='b') #plotting if necessary features
plt.plot(test,pre,color='black',linewidth=3) #plotting labels if necessary
plt.show

#one kilotone needs 45000 trees 
trees=pre*45000