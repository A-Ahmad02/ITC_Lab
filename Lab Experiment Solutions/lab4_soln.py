# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:09:51 2020

@author: hp
"""
# #%%
# #Q1
# z = int(input("Enter the number of times you want to print:"))
# y=1
# while (y<=z):
#     print("Hello World")
#     y+=1 
# #%%
# #Q2
# y=1   
# for y in range(1,4,1):
#     x = float(input("Enter a number:"))
#     if x<0:
#         x = -1*x
#     print("The absolute is",x)
    
# #%%
# #Q3
# print("12345678901234567890")    
# print("Integer   Square")   
# x=1 
# while (x<=10):
#    print("  ",x,"       ",x**2)
#    x=x+1   
# #%%
# print("12345678901234567890")    
# print(f'{"Integer":10}Square')   
# x=1 
# while (x<=10):
#    print(f'{"":3}{x}{"":9}{x**2}')
#    #print(f'{x:4d}{x**2:10d}')
#    x=x+1   
# #%%
# #Q4
# s = "1233"
# one=0
# two=0
# three=0
# print("In",s)
# for x in s:
#     if x=="1":
#         one=one+1
#     elif x=="2":
#         two=two+1
#     elif x=="3":
#         three=three+1
# print("The number of '1's is",one,"\nThe number of '2's is",two,"\nThe number of '3's is",three)
# #%%
# #Q5
# s = "12321"
# y = len(s)-1
# c = 0
# for x in range(0,2):
#     if s[x]==s[y]:
#         c=c+1
#     y = y-1   
# if c==2:
#    print("The number",s,"is a palindrome.")
# else:
#    print("The number",s,"is not a palindrome.") 
#%%
#Q5
s = "12321"
y = len(s)-1
c = 0
a = int((len(s)+1)/2)
for x in range(0,a):
    if s[x]==s[y]:
        c=c+1
    y = y-1   
if c==a:
   print("The number",s,"is a palindrome.")
else:
   print("The number",s,"is not a palindrome.") 



