#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:55:22 2019

@author: adalar
"""
# comment line
#%%
#variable
var1 = 10  #number
var2 = 15

gun = "pazartesi" #string

var3 = 10.0 #double 
#%%
#string

s = "bugun gunlerden pazartesi"

variable_type = type(s)
print(s)

var1 = "ankara"
var2 = "istanbul"
var3 = var1 + var2

var4 = "1001"
var5 = "2001"
var6 = var4 + var5

uzunluk = len(var6)
#%%
#number
#integer
intDeneme = -50

float_deneme = -30.7  #float and double
#%%
#function
#user defined

var1 =20
var2 = 50
output = (((var1 + var2)*50)/100.0)*var1/var2

def benim_ilk_fun(var1,var2):
    
    """     
    açıklama tanımı
    parametre:
    
    return:
    """
    output = (((var1 + var2)*50)/100.0)*var1/var2
    
    return output

sonuc = benim_ilk_fun(4,5)

def deneme1():
    print("ikinci fonk")
    
#%% default and flexible
def cember_cevre(r,pi=3.14):
    """
    input(parametre):r,pi
    çember çevre hesapla
    """
    output = 2*pi*r
    return output

#flexible
def hesapla(boy,kilo,*args):
    print(args)
    output = boy+kilo
    return output
    
#    def hesapla(boy,kilo,yas):
#        output = (boy+kilo)*yas
#        return output

#%% lambda funciton
    
def hesapla(x):
    output = x*x
    return output
sonuc = hesapla(3)

sonuc2 = lambda x: x*x
sonuc2(3)
    



#object
