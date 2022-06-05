#assignment 3
#1
print("enter your number:")
a=int(input())
c=bin(a)
print(c[2:])
#2
math_ex=input("enter a mathmatical expression")
print("result=",eval(math_ex))

#3(a)
import math
a=(3+4)*5
print(a)

#3(b)
print("enter your number:")
n=float(input())
a=(n*(n-1))/2
print(a)

#3(c)

rad=(float(input("enter the rad:")))
print(4*math.pi*rad**2)
#d
r=float(input("d))enter the value:"))
a=int(input("enter the value of a in degrees:"))
a=(a/180)*(math.pi)
b=int(input("enter the value of b in degrees: "))
b=(b/180)*(math.pi)
print(math.sqrt(r*(math.cos(a))**2 + r*(math.sin(b))**2))

#(e)
y2=float(input("enter the value of y2:"))
y1=float(input("enter the value of y1:"))
x2=float(input("enter the value of x2:"))
x1=float(input("enter the value of x1:"))
print((y2-y1)/(x2-x1))
#4

#(a)
for i in range(5):
    print(i,end=" ")
print("\n")
    
#b
for i in range(3,10):
    print(i,end=" ")
print("\n")

#c
for i in range(4,13,3):
    print(i,end=" ")
print("\n")
#d
for i in range(15,5,-2):
    print(i,end=" ")
print("\n")

#e
for i in range(5,3):
    print(i,end=" ")
print("\n")
    
#5
c=int(input("enter no of carbon:="))
o=int(input("enter no of oxygen:="))
h=int(input("enter the no of hydrogen:="))
m=1.00794*h+12.0107*c+15.9994*o
print("molecular weight is",m)