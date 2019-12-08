#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:40:16 2019

@author: adalar
"""
#%%  matplotlib görselleştirme kütüphanesi
#line plot, scatter plot, bar plot,sub plot, histogram
 

#iris datasında 5 feature var

import pandas as pd

df = pd.read_csv("iris.csv") #iri datası read edildi

print(df.columns)

##spiecs kaç tür olduğu tespit benzersiz olanları tespit et
print(df.Species.unique())  ##['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

print(df.info())

print(df.describe()) #numerik değerleri karşılaştır

setosa = df[df.Species == "Iris-setosa"]

versicolor =  df[df.Species == "Iris-versicolor"] 

print(setosa.describe())
print(versicolor.describe())

#%% line plot

import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1) ##id￼ alanını drop edip temizledik yeni df1

#df1.plot()  ##default line plot yapar
#plt.show() 

setosa = df[df.Species == "Iris-setosa"]
versicolor =  df[df.Species == "Iris-versicolor"] 
virginica = df[df.Species == "Iris-virginica"] 


## x , y , color, etiket
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa - PetalLengthCm")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="blue",label="versicolor - PetalLengthCm")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="green",label="virginica - PetalLengthCm")

plt.xlabel("id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()


df1.plot(grid=True, alpha = 0.9) ## alpha saydamlık
plot.show()

#%% scatter plot
## genelde iki özellik karşılaştırmak için kullanılır

setosa = df[df.Species == "Iris-setosa"]
versicolor =  df[df.Species == "Iris-versicolor"] 
virginica = df[df.Species == "Iris-virginica"] 

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label=setosa)
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="blue",label=versicolor)
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="green",label=virginica)

plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

#%% histogram plot
## istatiksel anlamda sıklıkla kullanılır

plt.hist(setosa.PetalLengthCm,bins=10)  ##frekansı
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

#%% bar plot
import numpy as np

#x = np.array([1,2,3,4,5,6,7])
#y = x*2+5
#
#plt.bar(x,y)
#plt.xlabel("x")
#plt.ylbale("y")
#plt.title("bar plot")
#plt.show()

x = np.array([1,2,3,4,5,6,7])
a = ["tr","usa","uk","gb","can","esp","ch"]
y = x*2+5

plt.bar(a,y)
plt.xlabel("x")
plt.ylbale("y")
plt.title("bar plot")
plt.show()

#%% subplot

df1.plot(grid=True,alpha= 0.9,subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
