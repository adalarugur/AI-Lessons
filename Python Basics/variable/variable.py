# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
#variable
var1 = 10
var2 = 15

day = "monday"

x = 12.0

var5 = 10
var7 = 19

# %%
#string
s = "this day monday"

variable_type = type(s)
print(s)

deg1 = "ank"
deg2 = "iz"
deg3 = deg1+deg2 #deg birleştirme

degA = "nasil bir degisken bu"
uzun =  len(degA)

# %%
#numbers

#integer 
int_try = -50

#double

float_try = -40.7

# %% built infunction

str1 = "try"

float1 = 10.6

str2 = "1005"

# %% user defined functions

var1 = 20
var2 = 50

#definition func sonra tab koyulur sonra code block yazılır
def my_first_fucn(x,y):
    """
    first try
    
    parametreler:
    
    return:    
    """
    output = ((((x+y)*50)/100.0)*x/y)%5
    
    return output

sonuc = my_first_fucn(var1,var2)
print(sonuc) 

def try2():
    print("second try")
#object
