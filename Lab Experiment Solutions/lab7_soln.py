# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:32:16 2022

@author: UET
"""
#Q1
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
#%%
#Q1
a = [ 2, 3, 5, 3, 7 ]

print("a =", a)

for index in range(len(a)):
    if (a[index] == 3):  
        a.pop(index)

print("This line will not run!")
#%%
#Q2
def calc(a,b):
    return (a+b,a-b,a*b,a/b)
a = 1
b = 2
(s,d,p,q) = calc(a,b)
print("The sum is",s,"\nThe difference is",d,"\nThe product is",p,"\nThe quotient is",q)
#%%
#Q3A
def add_lists(L1,L2):
    L3=[]
    for x in range(len(L1)):
        L3.append(L1[x]+L2[x])
    print('The element-wise sum of',L1,'and',L2,'is',L3)
L1=[1,2,3,6]
L2=[3,3,3,3]
add_lists(L1,L2)
#%%
#Q3B
L=[]
while(True):
    x=input('enter:')
    if x=='end':
        break
    L.append(int(x))
print("\nThe list is",L)
#%%
#Q3C
def create_list():
    L=[]
    while(True):
        x=input('enter:')
        if x=='end':
            break
        L.append(int(x))
    return L

def add_lists(L1,L2):
    L3=[]
    for x in range(len(L1)):
        L3.append(L1[x]+L2[x])
    print('The element-wise sum of',L1,'and',L2,'is',L3)

print("Enter elements of list L1")
L1 = create_list()
print("\nEnter elements of list L2")
L2 = create_list()
add_lists(L1,L2)
#%%
#Q4
def add_lists(L1,L2):
    L3=[]
    for x in range(len(L1)):
        L3.append(L1[x]+L2[x])
    return L3

c = [2,1,1]
d = [0,1,2]    
a=0
z=0
L2 = [0] * ( ( len(c) + len(d) ) - 1 )

for x in c:
    L1 = [0] * ( ( len(c) + len(d) ) - 1 )
    for y in d:
        L1[z] = x*y
        z=z+1
    L2 = add_lists(L1,L2)
    a=a+1
    z=a
    
if L2[0] == 0:
    L2.pop(0)
#%%
#Q5
def square(l):
    L = [([0]*2) for x in range(0,2,1)]
    
    for row in range(0,2,1):
        for col in range(0,2,1):
            L[row][col] = (l[row][col])**2
    
    print("The square of",l,"is",L)
    
l1 = [[1,2],[3,4]]
square(l1)
#%%
#Q6
def matrixMultiply(a,b):
    m=len(a)
    n=len(a[0])
    o=len(b)
    p=len(b[0])
    
    
    if n==o:
        c = [([0]*p) for x in range(m)]
            
        for i in range(0,m):
            for j in range(0,p):
                for k in range(0,n):
                    c[i][j] += a[i][k] * b[k][j]   
        return c
    
    else:
        return None
         
m1 = [[1,2],[3,4]]
m2 = [[1,2],[2,1]]
print(matrixMultiply(m1,m2))
