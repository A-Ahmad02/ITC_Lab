# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:15:25 2020

@author: hp
"""
#Task 1
import math
x = 2
y = 5
Sum = x + y
Product = x * y
Difference = y - x

print("The sum is",Sum,"\nThe product is",Product,"\nThe difference is",Difference)
#%%
#Task 2
"""This program calculates the average of three numbers entered by the user"""
x = float(input("Enter the 1st no.:")) #The first number entered by the user
y = float(input("Enter the 2nd no.:")) #The second number entered by the user
z = float(input("Enter the 3rd no.:")) #The third number entered by the user

average = (x+y+z)/3 #Average is calculated here

print("\nThe average is",average) #Average is displayed by this statement

#%%
#Task 3
a=int(input("""Enter 'a':\n"""))
b=int(input("""Enter "b":\n"""))
c=int(input("""Enter 'c':\n"""))
r1 = (-b + ((b**2)-(4*a*c))**(0.5)) / (2*a)
r2 = (-b - ((b**2)-(4*a*c))**(0.5)) / (2*a)
print("\nThe roots are",r1,"and",r2)

#%%
#Task 4
import math
a=50
c=10
alpha = math.acos(c/a) * (180/math.pi)
b=c*math.tan((alpha*math.pi)/180)
print("The value of alpha is",alpha,"\nThe value of c is",c,"metres\nThe value of b is",b)
#%%
#Task 5
a=10
b=5
c=15
d=20
theeta=45

x = ( (a/b) * math.sin( theeta * ( math.pi/180 ) ) ) ** ( a/b**2  )
y = ( (b/a) * math.cos( theeta * ( math.pi/180 ) ) ) ** ( 1/(a+b) ) 
z = (     c * math.tan( theeta * (math.pi/180) ) ) - ( d/c )
ans = ((x + y)**(0.5)) / z
print("The answer is" , ans)
#%%
x=2
y=5
print("Step1: x =",x,"y =",y)
x=x+1
print("Step2: x =",x,"y =",y)
y=y+1
print("Step3: x =",x,"y =",y)
x=x+y
y=x-y
print("Step4: x =",x,"y =",y)




