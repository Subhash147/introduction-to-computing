# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:43:27 2022

@author: subhash kumar
"""
  
#ASSIGNMENT 2ND

#1st question
String="Python is a case sensitive language"
print(len(String))

print(String[::-1])

print("new string:",String[10:26])
print(String.replace("a case sensitive", "object oriented"))
print(String.find("a"))
print(String.replace(" ",""))



#2nd question

var1="Subhash kumar"
var2=2110802
var3="metallurgical and meterials eng"
var4=7.3
print(F"hey {var1} here!")
print(F"MY SID is {var2}")
print(F"I am from {var3} department and my cgpa is {var4}")

#3 question

a=56
b=10
print("the ans of 1st que:",a&b)
print("the ans of  que 2nd:",a|b)
print("the ans of 3rd que:",a^b)
print("the ans of 4th que:",a<<2,b<<2)
print("the ans of 5th que:",a>>2,b>>2)

#4 question

print("type your sentence")
if "name" in input(str()):
    print("yes")
else:
    print("no")
    
#5th question


print("side_1st:")
side_1st=float(input())
print("side_2nd:")
side_2nd=float(input())
print("side_3rd")              
side_3rd=float(input())
a=(side_1st+side_2nd)
b=(side_2nd+side_3rd)
c=(side_1st+side_3rd)
check1=(a>side_3rd)
check2=(b>side_1st)
check3=(c>side_2nd)
answer=str(check1 & check2 & check3)
print(answer.replace("True","yes"))
print(answer.replace("False","no"))

#6th question

number1=int(input("enter first number"))
number2=int(input("enter your second number"))
ex_or=number1 ^ number2
bin_exor=bin(ex_or)
check_string=str(bin_exor)
A=check_string.count("1")
print(A)