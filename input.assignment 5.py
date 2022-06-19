# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 16:42:47 2022

@author: subhash kumar
"""
#1

str=input("enter the string:")
for i in range((len(str)-1),-1,-1):
    print(str[i],end="")
#2
lower=int(input("enter the lower no:"))
upper=int(input("enter the upper no:"))
number=int(input("enter the no by which we devide:"))
for i in range(lower,upper+1):
    if i%number==0:
        print(i)
    i=i+1
#3

a=float(input("enter the first side:"))
b=float(input("enter the second side:"))
c=float(input("enter the third side:"))

if (a+b<=c or b+c<=a or c+a<=b):
    print("traingle cant formed")
else:
    print("trng can be formed")
s=(a+b+c)/2
from math import sqrt
area=sqrt(s*(s-a)*(s-b)*(s-c))
print(area)


#4


n=5
for i in range(n):
    for k in range (i):
        print("*",end="")
    print("")
    
for i in range(n,0,-1):
    for k in range(i):
        print("*",end="")
    print("")
#5
n=int(input("enter the number for alphabets:"))
for i in range(n):
    for j in range(i+1):
        print(chr(j+65),end="")
    print()
#6
lower=int(input("enter the lower number:"))
upper=int(input("enter the upper number:"))
for i in range(lower,upper+1):
    if i%2==0:
        print("prime numbers are",i)
    i=i+1
#7
for i in range(1,501):
    if i%5==0 and i%7==0:
        print("number are ",i)
    i=i+1
    
#8
    
integers=list(input("Enter the 10 intergers (,)=").split(","))
for i in integers:
#type numbers to check the no is neg,prime, or positive
    i=int(input())
    if i<0 and i%2==0:
        print("i is a negative and prime")
        
    if i<0 and i%2!=0:
        print("negative and odd")
    if i>0 and i%2!=0:
        print("positive and odd")
        
    if i>0 and i%2==0:
        print("i is a postive number and prime")
    if i==0:
        print("zero")
    set_integers=set(integers)
    for i in set_integers:
        print(i,"appeared",integers.count(i),"times")


#9
user_list=input("enter the list sep by comma(,):")
word_list=user_list.split(",")
counts=dict()
for word in word_list:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts)
        
    
        