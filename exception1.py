# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:59:15 2024

@author: MERT
"""

#%% exceptions 

a = 10
b = 2

list = [1,2,3]

print(sum(list))
print(a+b)

k=10
zero = 0

#print(k/0) hata

if (zero == 0):
    a = 0
else:
    a = k/zero
    
try:
    a = k/zero
except ZeroDivisionError:
    a=0
    
#index error
list1 = [1,2,3,4]
#list1[15]

#module not found error

#import numpyy

#file not found error
import pandas as pd
#pd.read_csv("asd")

#type error

#"2" + 5


#value error
#int("sad")


try:
    1/1
except:
    print("except")
else:
    print("else")
finally:
    print("done")
    
s="fffggg"
print(s[::-2])

a = "zaa"

b = "maa"

print("aa" in 2*(a+b))

a = 5.5

b = 3

print(a//b)

print(int(51.88+4/5))

print(sum([1,2,3]))

def s(x, y = 2):

    return x**2

a = [[1,2,3],[3,2,1],[0,0,0]]

t = (1,2,3,4)