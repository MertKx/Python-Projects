# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:22:49 2024

@author: MERT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("decision+tree+regression+dataset.csv",sep=";",header=None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

#%% decision tree regression
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(x,y)

print(tree_reg.predict([[6]]))
x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = tree_reg.predict(x_)
#%% visualize 
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun level")
plt.ylabel("price")
plt.show()

#basamaklanmanin sebebi belirli bir terminal leafde y degerlerinin 
#ortalamasi ayni olacagindan belirli alanlarda duz bir cizgi
#yani sabit bir degere sahibiz







