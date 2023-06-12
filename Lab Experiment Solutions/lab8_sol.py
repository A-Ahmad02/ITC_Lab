# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 11:31:14 2022

@author: UET
"""
#Q1
def ct2(d, key):
    while (key in d) and ((key+2) not in d):
        d[key+2] = key+1
        key = d[key]
    L         = [ ]
    for key in  sorted(d.keys()):
        L.append(10*key + d[key])
    return L
print(ct2({1:5, 0:2}, 0))
#%%
#Q2
d = {"Lahore":"Punjab" , "Peshawar":"KPK" , "Karachi":"Sindh" , "Quetta":"Balochistan" , "Gilgit":"GB"}
city = input('Enter city:')

if city in d:
    print(city,"is in",d[city])
else:
    print(city,"is not in the dictionary")
#%%
#Q3
def add(x,y):
    
    d3={}
    for k in x:
        d3[k] = x[k] + y[k]
    return d3
    
d1 = {"a":50 , "b":5 , "c":10}
d2 = {"a":20 , "b":3 , "c":40}
print("The resultant dictionary is",add(d1,d2))
#%%
#Q4
def f(d):
    d1={}
    for k in d:
        s=0
        for x in d[k]:
            s = s+x
        avg = s/len(d[k])
        print("The average of",k,"is",avg)
        d1[k] = avg  
    print(d1)
D = {'Joe':[1,2,3] , 'John':[1,1,1] , 'Susan':[4,1,2,3]}
f(D)

#%%
#Q5
d  = {"Joe":"A" , "John":"A" , "Susan":"A"}
d1 = {"A":0 , "B":0 , "C":0}

x=0
a=0
b=0
c=0

for k in d:
    if d[k] == "A":
        a=a+1
    elif d[k] == "B":
        b=b+1
    elif d[k] == "C":
        c=c+1

L = [a,b,c]        

for k in d1:
    d1[k] = L[x]
    x=x+1
     
print("d = ",d)
print("d1 = ",d1)
#%%
#Q6
def mostFrequent(l):
    d = {}
    f =[]
    
    if l==[]:
        print("The list is empty")
    else:
        for k in l:
            d[k] = l.count(k)
        
        for k in d:
            if d[k] == max(d.values()):
                f.append(k)
        
        print("The list L is",l)
        print("The dictionary is",d)
        print('The number(s)',f,'occurs more frequently and its the frequency is',d[f[0]])
        


l = [5,100,21,5,1,3,10,10,3,10,5]
mostFrequent(l)




