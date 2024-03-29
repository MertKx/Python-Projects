# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:59:14 2024

@author: MERT
"""

# import library
import pandas as pd
import matplotlib.pyplot as plt

# import data
df = pd.read_csv("C:/Users/MERT/Desktop/Udemy AI/Linear Regression/linear_regression_dataset.csv",sep = ";")

# plot data
plt.scatter(df.deneyim,df.maas)
plt.xlabel("deneyim")
plt.ylabel("maas")
plt.show()

# linear regression

# sklearn library
from sklearn.linear_model import LinearRegression

# linear regression model
linear_reg = LinearRegression()

x = df.deneyim.values.reshape(-1,1)
y = df.maas.values.reshape(-1,1)

linear_reg.fit(x,y)

y_head = linear_reg.predict(x)  # maas

plt.plot(x, y_head,color = "red")


#r-square
from sklearn.metrics import r2_score

print("r_square score: ", r2_score(y,y_head))


















