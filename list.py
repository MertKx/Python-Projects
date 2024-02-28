# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:53:10 2024

@author: MERT
"""

#%%
#list

list = [1,2,3,4,5,6]
print(type(list))

stringList = ["ptsi" , "sali" , "crs"]
print(type(stringList))

value = list[0]
print(value)

#%%
#dictionary

dictionary = {"okan":21,"salih":18,"osman":54}
print(dictionary["okan"])
print(dictionary.keys())
print(dictionary.values())


def deneme():
    dictionary1 = {"okan":21,"salih":18,"osman":54}
    return dictionary1
dic = deneme()
print(dic)

#%% CONDITIONALS
#if else statements
var1 = 10
var2 = 20

if(var1>var2):
    print("Var1 is bigger than var2")
elif(var1 ==var2): 
    print("These numbers are equal")
else:
    print("var1 smaller than var2")

list = [1,2,3,4,5]
value = 2

if value in list:
    print("Yeap we have {} in list".format(value))
else:
    print("We do not have")

dictionary = {"Mert":30,"Soner":40}
keys = dictionary.keys()
if "Mert" in keys:
    print("Yeah")
else:
    print("No!")

#%%
#quiz time
year = 1940
def yuzyil(year):
    """
    Parameters:
    year 
    Returns:
    Which century
    """
    
    yearStr = str(year)
    if (len(yearStr)<3):
        return 1
    elif(len(yearStr) ==3):
        if(yearStr[1:3] == "00"): #100,200
            return int(yearStr[0])
        else:                     #190,205
            return int(yearStr[0])+1
    else:                          #1870 1700
        if(yearStr[2:4]=="00"):    #1900 1500
            return int(yearStr[:2])
        else:
            return int(yearStr[:2])+1

yuzyil(1800)
yuzyil(2005)
yuzyil(999)
yuzyil(1001)
#%%loops
for i in range(1,11):
    print(i)
    
for each in "Mert geldi":
    print(each)
    
for each in "Hi guys".split():
    print(each)
    
list = [1,2,4,5,8,7,9,5,2,4]

summation = sum(list)
print(summation)    

count = 0
for each in list:
    count = count + each
print(count)

#while loop

i = 0
while(i<4):
    print(i)
    i += 1

border = len(list)
each = 0
count = 0
while (each < border):
    count += list[each]
    each += 1
    print(count)
    
#%%
# last quiz

#we will find smallest value in given list

list = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]
smallest = 0
for i in list:
    if (i <= smallest):
        smallest = i
print("Your smallest value is: {}".format(smallest))

# then we will find biggest value in given list
biggest = 0
for i in list:
    if (i>=biggest):
        biggest=i
print("Your biggest value is {}".format(biggest))








