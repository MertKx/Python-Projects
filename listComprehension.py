# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:47:12 2024

@author: MERT
"""

# List Comprehension Examples
list1 = [1,2,3,4,5]
list2 = [i*2 for i in list1]

print(list2)

#List Comprehension in string variables
names = ["Orha", "Cana" , "Kena", "Oka"]
remains = [i+"n" for i in names]

print(remains)

#conditional list comp

num1 = [40,30,22]
num2 = [i*2 if i%5 == 0 else i-2 if i>20 else i+1 for i in num1]
print(num2)