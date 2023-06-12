# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:13:58 2021

@author: UET
"""
#Q1
def add():
    x=1
    y=2
    print("The sum is",x+y)

def sub(x,y):
    print("The difference is",x-y)

def mul(x,y):
    return(x*y)

def div():
    x=1
    y=2
    return (x/y)

add()
sub(1,2)
print("The product is",mul(1,2))
print("The quotient is",div())
#%%
#Q2
def square():
    print("Square\n***\n***\n***")
def rectangle():
    print("Rectangle\n****\n****\n****")

square()
rectangle()
#%%
#Q3
def grade(marks):
    if marks > 15:
        return "A"
    elif (x > 10) and (x <= 15):
        return "B"
    elif (x > 5) and (x <= 10):
        return "C"
    elif (x >= 0) and (x <= 5):
        return "F"
    
x = float(input("Enter marks:"))
print("Grade is ", grade(x))
#%%
#Q4
def square(x):
    y=x*x
    return y
	
def sum_of_squares(x, y, z):
	a = square(x)
	b = square(y)
	c = square(z)
	
	return a + b + c
	
a = -5
b = 2
c = 10

print("The sum of square is",sum_of_squares(a, b, c))
#%%
#Q5
def calc(x,y):
    def add(c,d):
        return(c+d)
    
    def sub(c,d):
        return(c-d)
    
    def mul(c,d):
        return(c*d)
    
    def div(c,d):
        return (c/d)
    
    print("The sum is",add(x,y))
    print("The difference is",sub(x,y))
    print("The product is",mul(x,y))
    print("The quotient is",div(x,y))

def shape():
    def square():
        print("Square\n***\n***\n***")
    def rectangle():
        print("Rectangle\n****\n****\n****")
    print("")
    square()
    print("")
    rectangle()
a=1
b=20
calc(a,b)
shape()


#%%
#Q6
def pyr(y):
    r=int(y)
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

x="a"
while(x!="stop"):
    x = input("Enter: ")
    if x == "stop":
        break
    pyr(x)


