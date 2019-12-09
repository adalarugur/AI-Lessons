#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:45:09 2019

@author: adalar
"""

class Calisan:
    
    zamOrani = 1.8
    counter = 0
    def __init__ (self,isim,soyisim,maas):  #constructur
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@oopsmail.com"
        Calisan.counter = Calisan.counter + 1
        
    def giveNameSurname(self):
        return self.isim + " " + self.soyisim
    
    def zamYap(self):
        self.maas = self.maas + self.maas*self.zamOrani

#isci1 = Calisan("ali","atabak",100)
#
#print(isci1.giveNameSurname())

#%% class variable

calisan1 = Calisan("abu","kumalov",100)

print("ilk maas",calisan1.maas)
calisan1.zamYap()
print("sonmaas", calisan1.maas)

calisan2 = Calisan("ali","mahoxuv",200)
calisan3 = Calisan("aysa","orhan",600)
calisan4 = Calisan("fatma","gorhov",500)


#%% classs example
    
liste = [calisan1,calisan2,calisan3,calisan4]

maxiMaas = -1
index = -1

for each in liste:
    if(each.maas > maxiMaas):
        maxiMass = each.maas
        index = each
print(maxiMaas)
print(index.giveNameSurname())
