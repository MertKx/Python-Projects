# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:00:15 2024

@author: MERT
"""

#Pandas

import pandas as pd

#whats a dataframe
dictionary = {"Name": ["Aliye","Osman","Tahir","Hasan","Mert","Bilal"],
              "Age": [15,16,17,33,45,66],
              "Salary":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()
tail = dataFrame1.tail()
#%% 
#Basic methods in pandas

#print(dataFrame1.columns) #gives columns

print(dataFrame1.info())

print(dataFrame1.dtypes)

print(dataFrame1.describe())

#%% indexing - slicing

print(dataFrame1["Name"])
print(dataFrame1.Age)

dataFrame1["NewFeature"] = [-1,-2,-6,-4,-5,-6]

print(dataFrame1.loc[:, "Age"])
print(dataFrame1.loc[1:3, "Age"])
print(dataFrame1.loc[:3, ["Age","Name"]])

print(dataFrame1.loc[::-1,:])

print(dataFrame1.loc[:,:"Name"])

print(dataFrame1.iloc[:,2])


#%% filtering

filter1 = dataFrame1.Salary > 150

filteredData = dataFrame1[filter1]

filter2 = dataFrame1.Age < 20

dataFrame1[filter1 & filter2]

print(dataFrame1[dataFrame1.Age>60])

#%% list comprehension
import numpy as np

avgSalary = dataFrame1.Salary.mean()

#avgSalaryNp = np.mean(dataFrame1.Salary) #calculating average using numpy

dataFrame1["Salary Level"] = ["Yuksek"if each > avgSalary else "dusuk" for each in dataFrame1.Salary]


# for each in dataFrame1.Salary:
#     if(avgSalary > each):
#         print("Yuksek")
#     else:
#         print("Dusuk")


dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if (len(each.split())>1) else each for each in dataFrame1.columns]

#%% drop and concatenating

#dataFrame1.drop(["newfeature"],axis=1,inplace = True)

data1=dataFrame1.head()
data2=dataFrame1.tail()

#vertical

data_concat = pd.concat([data1,data2] , axis=0)

#horizontal

maas = dataFrame1.salary
age = dataFrame1.age

data_h_concat = pd.concat([salary,age],axis=1)
#%% Transforming data

dataFrame1["list_comp"] = [each*2 for each in dataFrame1.age]

#apply

def multiply(age):
    return age*2

dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)





