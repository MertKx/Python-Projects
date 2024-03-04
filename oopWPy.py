# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:15:32 2024

@author: MERT
"""

class Calisan:
    
    zamOrani = 1.8
    counter = 0
    
    def __init__(self,isim,soyisim,maas): #constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@gmail.com"
        
        Calisan.counter += 1
        
    def giveNameSurname(self):
        return self.isim+" "+self.soyisim
    
    def zamYap(self):
        self.maas += self.maas*self.zamOrani
    
#isci1 = Calisan("Mert","Kalay",100)
#print(isci1.giveNameSurname())

#class variable
calisan1 = Calisan("Mert", "Kalay", 100)
print("ilk maas: " ,calisan1.maas)
calisan1.zamYap()
print("Yeni maas: ",calisan1.maas)

calisan2 = Calisan("Okan","Serbest", 120)
calisan3 = Calisan("Orhun","Yildiz", 320)
calisan4 = Calisan("Ceren","Gunes", 420)

#list
list = [calisan1,calisan2,calisan3,calisan4]


maxMaas = -1
index = -1
for each in list:
    if(each.maas>maxMaas):
        maxMaas = each.maas
        index = each
print(maxMaas)
print(index.giveNameSurname)


class A:

    global a

    a = 5

    def __init__(self,x = 4):

        self.x = x

    def sum(self):

        return a + self.x

x = A(5)










