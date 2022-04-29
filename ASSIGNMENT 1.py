#1
print("enter your 1st number:")
n1=int(input())
print("enter your 2nd number:")
n2=int(input())
print("enter your 3rd number:")
n3=int(input())
av=(n1+n2+n3)/3
print("average of these three numbers is:",av)


#2
Gross_Income=int(input("enter your income="))
tax_rate=0.2
no_of_depedents=int(input("enter no of dependents:",))
standard_deduction=10000
dependent_deduction=3000
Taxable_Income=Gross_Income-standard_deduction-(dependent_deduction*no_of_depedents)
print("Taxable_Income:",Taxable_Income)
Tax=Taxable_Income*tax_rate
print("Tax:",Tax)

#3

sid=int(input("enter your sid=",))
name=input("enter your name=",)
gender=input("enter your gender=",)
course_name=input("enter your course name=",)
cgpa=float(input("enter your cgpa=",))
student=[sid,name,gender,course_name,cgpa]
print(student)

#4
s1=float(input("enter_1st_student_marks:"))
s2=float(input("enter 2nd student marks:"))
s3=float(input("enter 3rd student marks:"))
s4=float(input("enter 4th student marks:"))
s5=float(input("enter 5th student marks:"))

marks_of_students=[s1,s2,s3,s4,s5]
marks_of_students.sort()
print(marks_of_students)


#5
#Part a

color=["Red","Green","White","Black","Pink","Yellow"]
color.remove("Black")
print(color)

#Part b

color=["Red","Green","White","Black","Pink","Yellow"]
color[3:5]=["Purple"]
print(color)