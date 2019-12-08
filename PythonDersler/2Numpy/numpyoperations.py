#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:43:45 2019

@author: adalar
"""
import numpy as np

a = np.array([1,2,3])

b = np.array([4,5,6]) #aynı uz boy olma şartı

print(a+b)
print(a-b)
print(a**2) #karesi

print(np.sin(a))

print(a<2)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

print(a*b) #element wise product

a.dot(b.T)  #tranpoze alma

a = np.random.random((5,5))

a.sum()
a.max()
a.min()


print(a.sum(axis=0)) #sütünları topla
print(a.sum(axis=1)) #satırları topla

print(np.sqrt(a)) #karesini al
print(np.square(a)) #karekök al

print(np.add(a,a))
#%% indexing and slicing

array = np.array([1,2,3,4,5,6,7])

print(array[0])

print(array[0:4])

reverse_array = array[::-1] #ters çevir
print(reverse_array)

array1 = np.array([[1,2,3,4,5],
                   [6,7,8,9,10]])
print(array1[1,1])

print(array1[:1])

print(array1[1,1:4])

print(array[-1:])

#%%shape manupilation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.shape)

a = array.ravel()  #arrayı vektör hale getirir

array2 = a.reshape(3,3) #tekrar 3x3 lük hale getirdik

arrayT = array2.T    # transpoze alma  1,4,7  2,5,8 3,6,9

print(arrayT.shape)


array5 = np.array([[1,2],[3,4],[5,6]])
#resize   direk konsolda array5 i işaretler ve değştirir
#%% stacking array ,arrayleri birleştirme 

array1 = np.array([[1,2],
                   [3,4]])

array2 = np.array([[-1,-2],
                   [-3,-4]])

#vertical
array3 = np.vstack((array1,array2))

#horizontal
array4 = np.hstack((array1,array2))

#%% array convert arrayden liste listen arraya convert etme

liste = [1,2,3,4]

array = np.array(liste) #nparray

liste2 = list(array) #listeye çevir


a = np.array([1,2,3])  
## referams manığı b array değişince referns gidip diğerlerinide değiştirir
## memoryde aynı alanı ayırdığın için 

b = a
c = a

d = np.array([3,6,9])
e = d.copy()  # memoryde yeni alan



