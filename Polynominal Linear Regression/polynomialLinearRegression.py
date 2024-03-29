# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:10:36 2024

@author: MERT
"""

#importing

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("polynomial+regression.csv",sep=";")

y = df.araba_max_hiz.values.reshape(-1,1)
x = df.araba_fiyat.values.reshape(-1,1)

plt.scatter(x,y)
plt.ylabel("araba_max_hiz")
plt.xlabel("araba_fiyat")
plt.show()

#linear regression y=b0+b1*x
#multiple linear regression y=b0+b1*x1+b2*x2


#%% linear regression

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x,y)



#%% predict
y_head = lr.predict(x) #x arrayinin her degerine gore prediction yaptik

plt.scatter(x, y)
plt.plot(x, y_head, color="red",label="linear") 
plt.legend()# Kırmızı çizgiyi scatter grafiğine çizdiriyoruz
plt.ylabel("araba_max_hiz")
plt.xlabel("araba_fiyat")
plt.show()

print(lr.predict([[510]]))

#%%
#polynomial regression y=b0+b1*x+b2*x^2

from sklearn.preprocessing import PolynomialFeatures

polynomial_regression = PolynomialFeatures(degree=4) #degree us degeri
#degree arttikca egim artacagindan daha az hatali bi grafik olur


x_polynomial = polynomial_regression.fit_transform(x)
#buradaki transform benim ximi ikinci dereceden x^2 ye cevir demek
# fit ve transform yani uygula ve cevir

#%% fit
linear_regression2 = LinearRegression()
linear_regression2.fit(x_polynomial,y)

#%% visualization
y_head2 = linear_regression2.predict(x_polynomial)

plt.plot(x,y_head2,color="black",label="poly")
plt.legend()
plt.show()

#%% graphs
# Linear regression grafiği
plt.scatter(x, y)
plt.plot(x, y_head, color="red", label="linear")
plt.legend()
plt.xlabel("araba_fiyat")
plt.ylabel("araba_max_hiz")
plt.show()

# Polynomial regression grafiği
plt.scatter(x, y)
plt.plot(x, y_head2, color="green", label="poly")
plt.legend()
plt.xlabel("araba_fiyat")
plt.ylabel("araba_max_hiz")
plt.show()











