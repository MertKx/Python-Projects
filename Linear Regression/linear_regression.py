# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:16:59 2024

@author: MERT
"""
# import libraries
import pandas as pd
import matplotlib.pyplot as plt

#import data
df = pd.read_csv("C:/Users/MERT/Desktop/Udemy AI/Linear Regression/linear_regression_dataset.csv",sep=";")

#plotting data
plt.scatter(df.deneyim,df.maas)
plt.xlabel("deneyim")
plt.ylabel("maas")
plt.show()

#%% linear regression

#sklearn library
from sklearn.linear_model import LinearRegression

#linear regression model
linear_reg = LinearRegression()

x = df.deneyim.values.reshape(-1,1)
y = df.maas.values.reshape(-1,1)

linear_reg.fit(x,y)

#%% prediction

import numpy as np

b0 = linear_reg.predict([[0]]) 

print("b0 = ", b0)

b0_ = linear_reg.intercept_
print("bo_: " ,b0)              #x=0 iken y=b0+b1*x 
                             #oldugundan y yi kesitigi nokta b0 dir

b1 = linear_reg.coef_
print("b1: " ,b1)  #egim 

# maas = 1663+1138*deneyim

maas_yeni = 1663 + 1138*11 #11 yillik birinin maasi
print(maas_yeni)

print(linear_reg.predict([[11]])) #2d yaptik [[]] ile

array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1) #deneyim

plt.scatter(x,y)
plt.show()

y_head= linear_reg.predict(array) #maas

plt.plot(array, y_head,color="red")

linear_reg.predict([[100]]) #100 yillik birinin maasi









