#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:05:04 2019

@author: adalar
"""

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) #1x15 lik vektör matris

print(array.shape)

a = array.reshape(3,5)
print("shape" , a.shape)

print("dimension" , a.ndim) #2 boyutlu dizi

print("size", a.size)

print("type" , type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[8,8,7,6]])

zeros = np.zeros((3,4))

zeros[0,0] = 5
print(zeros)


np.ones((2,3))

np.empty((2,4))


a = np.arange(10,50,5) #artırma 5 er 

b = np.linspace(10,50,20) #araya 20 tane sayı yazar


