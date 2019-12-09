#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:24:46 2019

@author: adalar
"""

##dataframe için oluşturulmuştur
# pandas hızlı ve etkili  dataframes sağlar

# dosyalar arasında geçişler basittir  csv text açıp inceleyip
#sonuçlarıda bu dosya tiplerine kaydedebilir geçişi kolay sağlar.

# veri içerisinde tüm değerler olmak zorunda değil,
# nonvalue olan durumlarda missing datalarda çözüm üretmeyei sağlar

#reshape yaparak datayı daha iyi kullanılabilir hale getirebiliriz
#slicing ve indexing kolay yapılır datadan belirli alan seçme

#timeseries datalarda , x zaman , y hız örneği gibi   timseries depolar
# ve yine analizinde yardımcı olur

# en önemlisi hızlıdır !!!! 

import pandas as pd 
dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,110,220]}

dataframe1 = pd.DataFrame(dictionary) #ilkdataframe

head1 = dataframe1.head() #dataframe içinde baştan 5 satırı ver, içinde belirtilen sayı kadar getirir yine
tail = dataframe1.tail()  #sondan 5 satırı ver içine belirteceğin kadar sondan alır yine

#%%pandasbasics

print(dataframe1.columns) #kolonlar, filtreleme için gereklidir

print(dataframe1.info()) #dataframe hakkında bilgi almayı sağlar

print(dataframe1.dtypes) #colon types

print(dataframe1.describe()) #sadece numerik özellileri getirir age ve maas kolonu buna örnek

#%% indexing and slicing belirli alanları seçme devam

print(dataframe1["NAME"]) #sadece ilgili kolondaki verileri aldım

print(dataframe1.AGE)

dataframe1["yeni_feature"] = [-1,-3,-5,-7,-9,-11]

print(dataframe1.loc[:,"AGE"]) #numpydaki gibi yüm satırlar ilgili sütün


print(dataframe1.loc[:3,"AGE"]) #burda 3 dahil oluyor

print(dataframe1.loc[:3,"AGE":"NAME"])

print(dataframe1.loc[::-1,:]) #tersten yazdır

print(dataframe1.loc[::,"NAME"]) #NAME DAHİL ORAYA KADAR TÜM SATIRLARI YAZDIR

print(dataframe1.iloc[:,2]) #kolonun indexini yazdık

#kalıp dataframe.loc 

#%% pandas ile filtering 
## true false boolean serilee değinildi, boolean seri elde etme
##belirli özelliklere göre filtre yapıyoruz

filtre1 = dataframe1.MAAS > 200

filtrelenmişData = dataframe1[filtre1] ##veriyi filtreledik frame yaptık

filtre2 = dataframe1.AGE<20

sonData = dataframe1[filtre1 & filtre2]  ## iki özellik birleştirme

print(dataframe1[dataframe1.AGE>60])  ## best pratices yazma şekli

#%% list comprehension

##ortalama maaşı bulalım
import numpy as np
ortMaasNp = np.mean(dataframe1.MAAS) ## yine numpy yöntemiyle

ortMaas = dataframe1.MAAS.mean() #ortalama alma

dataframe1["maas_seviyesi"] = ["yüksek" if ortMaas > each else "dusuk" for each in dataframe1.MAAS]
#yeni kolon eklendi şartlara göre alanlar dolduruldu

dataframe1.columns = [ each.lower() for each in dataframe1.columns] 

dataframe1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataframe1.columns]## string alanları küçük harfe çevirir

##örnek çöz


#%% concatenanting and drop
dataframe1.drop(["yeni_feature"],axis=1,inplace = True)

##inplace burada dataframe e eşitleme mantığında


#concateining birleştirme mantığı yine

data1 = dataframe1.head()
data2 = dataframe1.tail()

#dikey birleştir
data_concat = pd.concat([data1,data2],axis=0)


#yatay birleştir

maas = dataframe1.maas
age = dataframe1.age

data_h_concat = pd.concat([maas,age],axis=1)

#%%  transforming data

dataframe1["list_comp"] = [each*2 for each in dataframe1.age]
## yaşın 2 katını yazdık compr. yöntemle

def multiply(age):
    return age*2

dataframe1["apply_metodu"] = dataframe1.age.apply(multiply)






