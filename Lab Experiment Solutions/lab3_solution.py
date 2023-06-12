# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:56:24 2020

@author: hp
"""
#Q1

x = 4
if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#%%
#Q2
x = float(input("Enter marks:"))

if x > 15:
    print("The Grade is A")
elif (x > 10) and (x <= 15):
    print("The Grade is B")
elif (x > 5) and (x <= 10):
    print("The grade is C")
elif (x >= 0) and (x <= 5):
    print("The grade is F")
else:
    print("Invalid input")
#%%
#Q3
x = float(input("Enter a number:"))
print("The absolute of",x,"is",end=" ")
if x < 0:
    x = -x
print(x)
#%%
#Q4   
a = int(input("""Enter coeffecient 'a':"""))
b = int(input("""Enter coeffecient 'b':"""))
c = int(input("""Enter coeffecient 'c':"""))

d  = (b**2) - (4*a*c)
x1 = (-b + (d**0.5) ) / (2*a)
x2 = (-b - (d**0.5) ) / (2*a)

if d > 0 or d < 0:
    print("\nThe number of roots is 2")
else:
    print("\nThe number of roots is 1")

print("\nThe roots are",x1,'and',x2)

#%%
#Q5
x = input('Enter X:')
y = input('Enter Y:')
if ( (x=="T" or x=="t") and (y=="T" or y=="t") ):
    print("\nX and Y = True")
elif ( ( (x=="F" or x=="f") and (y=="F" or y=="f") ) or ( (x=="F" or x=="f") and (y=="T" or y=="t") ) or ( (x=="T" or x=="t") and (y=="F" or y=="f") ) ):
    print("\nX and Y = False") 
else:
    print("\nInvalid input")

#%%
n=10

if (n<10):
    
    if n==1:
        print("The no is 1")
    else:
        print("The no is greater than 1")
        
elif (n>=10 and n<=15):
    
    if (n==10):
        print("The no is 10")
    elif (n==11):
        print("The no is 11")
    else:
        print("The no is greater than 11 but less than 15")
        
else:
    print("The no is greater than 15")


