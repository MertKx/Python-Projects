# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:17:52 2024

@author: MERT
"""

# %%
#varibles (degiskenler)

a=10
b=20  #integers

isim = "Mert" #string

number = 10.4 #float
# %% 

# %%
#string

#printing strings
s = "herkese selamlar"
print(s)

#printing type of variables
variableType = type(s)
print(variableType)

#printing sum of two strings
var1 = "Ankara"
var2 = "Ist"
var3 = var1+var2
print(var3)

var4 = "100"
var5 = "200"
var6 = var4+var5
print(var6)

#calculating length of a string
print(len(var6))

#printing indexes in strings
length = var6
print(length[0])

#%%

#%% Numbers

#integer float

#printing integers
intTry = -50
print(intTry)

#printing floats
floatTry = -57.12
print(floatTry)

#changing between integer and float
number = float(10)
print(number)
print(type(number))

#printing strings
myName = "Mert"
print(myName)
print(type(myName))

#%%

#built-in functions

#changing variable types
str = "1005"
print(type(int(str)))

#rounding numbers
float = 10.6
print(round(float))

#%% 
#User Defined Functions

var1 = 20
var2 = 50

def function(a,b):
    """
    Parameters
    ----------
    var1 : TYPE
        DESCRIPTION.
    var2 : TYPE
        DESCRIPTION.
    Returns : Answer of calculation
    """
    output = (((a+b)*50)/100)*a/b
    
    return output

result = function(var1,var2)
print(result)

def function1():
    print("Bu bir deneme fonksiyonuydu")
    
function1()

#%%

#%%
# default and flexible functions

#default
def calculateCircleAround(r,pi = 3.14):
    """
    Parameters
    ----------
    pi,
    r : radius of circle.

    Returns : around of circle
    -------
    """
    output = (2*pi*r)
    return output 

calculateCircleAround(2)

#flexible

def calculate(length,weight,*args):
    """
    Parameters
    ----------
    length :
    weight :
    Returns : weight + lenght
    -------
    """
    print(args)
    output = (length+weight)*args[0]
    return output

# def calculate(length,weight,age):
#     """
    

#     Parameters
#     ----------
#     length :
#     weight :
#     age :
#     -------
#     returns: (weight+lenght)*age
#     """
#     output= (weight+length)*age
#     return output

calculate(1,2,5)
#%%
#%%
# QUIZ

# int variable yas
# string name isim
# fonksiyon yazicaz
# fonksiyon print(type(),len,float())
# *args soyisim
# default parametre ayakkabi numarasi

yas = 10
name = "Mert"
soyisim = "Kly"

def functionQuiz(yas,name,*args,ayakkabi=20):
    """
    Parameters
    ----------
    yas :
    name : 
    ayakkabi :The default is 20.
    *args : 
    Returns
    -------
    """
    print("Cocugun ismi: " , name, "yasi: " , yas,"ayak numarasi: " , ayakkabi )
    print(type(name))
    print(float(yas))
    
    output = args[0] * yas
    return output

sonuc = functionQuiz(yas, name, soyisim)
print("args[0]*yas: " , sonuc)
#%%















