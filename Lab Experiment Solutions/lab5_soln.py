# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:59:54 2020

@author: hp
"""
#Q1
for i in range (1,6):
    for j in range(1,i+1):
        print(i,end="")
    print("")
#%%
#Q2
for x in range(1,4,1):
    for y in range(1,4,1):
        print("(",x,",",y,")",end=" ")
    print("")
#%%
#Q3
r=int(input("Enter no. of rows of the pyramid: "))
a=r-1
b=1

for x in range(0,r,1):
    for y in range(0,a,1):
        print(" ",end="")
    for z in range(0,b,1):
        print("*",end="")
    print("")    
    a=a-1
    b=b+2
#%%
#Q4
            
rows=int(input("Enter no. of rows: "))
space=(rows-1)//2
stars=1

for i in range((rows+1)//2):
    for j in range(space):
        print(" ",end="")
    for k in range(stars):
        print("*",end="")
    space=space-1
    stars=stars+2
    print()

stars=rows-2
space=1

for i in range((rows-1)//2):
    for j in range(space):
        print(" ",end="")
    for k in range(stars):
        print("*",end="")
    space=space+1
    stars=stars-2
    print()


#%%
#Q5
a=0
b=0
c=0
for x in range(1,3,1):
    for y in range(1,4,1):
        for z in range(1,5,1):
            a = a + 0.395
        b = b + 0.495
    c = c + 0.595