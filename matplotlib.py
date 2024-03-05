# -*- coding: utf-8 -*-
"""

"""

# matplotlib kutuphanesi
# gorsellestime kotuphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv(r"C:\Users\MERT\Desktop\Udemy AI\Python-1\iris.csv")
 #dataframea cevirdik

print(df.columns)

print("---------------")

print("Unique turleri yazar")
print(df.Species.unique())

print("---------------")

print(df.info())

print("---------------")

print(df.describe())

print("---------------")

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())

print("---------------")
print(versicolor.describe())

print("---------------")

# %% Line plots
import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm,color="blue",label= "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="red",label= "virginica")
plt.legend() #labeli yerine koyar
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()


df1.plot(grid=True,alpha= 0.9,linestyle=":") #alpha = opacity
plt.show()


#%% scatter plot

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

# %% histogram

plt.hist(setosa.PetalLengthCm,bins= 20)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

# %% bar plot

import numpy as np

#x = np.array([1,2,3,4,5,6,7])
#
#y = x*2+5
#
#plt.bar(x,y)
#plt.title("bar plot")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()


x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","a","b","v","d","s"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% subplots

df1.plot(grid=True,alpha= 0.9,subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.show()

