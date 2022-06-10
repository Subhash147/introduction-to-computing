# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:06:30 2022

@author: subhash kumar
"""
print("enter the marks")
marks=int(input())
if marks<25:
    print("F")
elif 25<=marks<=45:
    print("E")
elif 45<marks<=50:
    print("D")
elif 50<marks<=60:
    print("C")
elif 60<marks<=80:
    print("B")
else:
    print("A")
    
#2
print("enter the year:")
year=int(input())
if year%4==0:
    print(year,"leap year")
elif year%400==0:
    print(year,"leap year")
elif year%100==0:
    print(year,"not a leap year")
else:
    print("not a leap year")



#3

import random
import math

i = 0
while i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    problem = int(input("Question {} : {} * {} =".format(i+1,num1,num2)))
    if problem == num1*num2:
        print("Your Ans Is Right")
    else:
        print("Your Ans Is Wrong. The Answer Is ", num1*num2)
    i=i+1
        
#4
for candies in range(200):
    if candies%5==2:
        if candies%6==3:
            if candies%7==2:
                print(candies,"candies are in the bowl")
                
            
          
    