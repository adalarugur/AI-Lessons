#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:16:42 2019

@author: adalar
"""

#%%
#list

liste = [1,2,3,4,5]
type(liste)

liste_str = ["pzt","salı","cars"]
type(liste_str)

liste[0:3]

liste[-1]

liste.append(7)

liste.remove(7)

liste.reverse()

liste2 = [1,2,7,4,9,6,3,8]
liste2.sort()

#%%  
#tuple

t = (1,2,3,4,5,6)

t.count(3) #kaç tane var
t.index(6) ## sayının indexini bul

#%% dictionary

dictionary = {"ali":32,"veli":25,"ayse":17}

def deneme():
    dictionary = {"ali":32,"veli":25,"ayse":17}
    return dictionary

dic = deneme()

#%% if else

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 büyük var2")
elif(var1 == var2):
    print("eşitler")
else:
    print("var1 küçük var2")    


liste = [1,2,3,4,5]


value = 6
if value in liste:
    print("içinde var".format(value))
else:
    print("içinde yok")
    
keys = dictionary.keys()

if "ali" in keys:
    print("evet")
else:
    print("hayır")
    
#%% 
    
def year2Century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
            return int(str_year[0])
        else:                       # 190, 250, 450
            return int(str_year[0])+1
    else:                           # 1750, 1700, 1805
        if(str_year[2:4]=="00"):    # 1700, 1900, 1100
            return int(str_year[:2])
        else:                       # 1705, 1645, 1258
            return int(str_year[:2])+1
            
#%% forloop        
for each in range(1,11):
    print(each)

for each in "ankara ist":
    print(each)

for each in "ankara ist".split():
    print(each)

liste = [1,4,5,6,8,9,77]

sum(liste) ##kısa yol built in funciton

count = 0
for each in liste:
    count = count + each
    print(count)

#%% while loop
i = 0
while(i<4):
    print(i)
    i = i+1
    
sinir = len(liste)
each = 0
while(each<sinir):
    count= count + liste[each]
    each = each + 1
#%% listede en küçük sayı bulma

liste = [2,3,4,5,12,44,55,-500,67,54,89]
mini = 100000
for each in liste:
    if(each < mini):
        mini = each
    else:
        continue
print(mini)
    











