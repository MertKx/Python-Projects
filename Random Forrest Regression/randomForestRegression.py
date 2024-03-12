# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:31:15 2024

@author: MERT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("random+forest+regression+dataset.csv",sep=";",header=None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)


#%%
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 100, random_state=42 )
#n_estimators metodu kac tane decision tree kullanilacagini belirler

#modelin her çalıştırıldığında kullanacağı rastgele sayı üreteci için başlangıç 
#durumunu belirleyen bir sayıdır. Bu, modelin veri kümesini rastgele bölerken veya
#diğer rastgelelik kullanan işlemleri gerçekleştirirken kullanılır.

rf.fit(x,y)
print("7.5 seviyesindeki fiyat: ",rf.predict([[7.5]]))

x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = rf.predict(x_)

#visualize
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun level")
plt.ylabel("price")
plt.show()


#100 adet decision tree kullanarak tahminler yaptik 





