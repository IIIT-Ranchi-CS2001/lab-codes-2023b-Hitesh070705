#Question 1
S1="Maha Bharat"
print(S1.swapcase())
print(S1[5:11])
print((S1[5:11])*3)
print(S1.replace("Maha","Mera"))
print(S1.replace("Maha","Mera") + "Mahan")

#Qusetion 2
S="Ba Ba Black Sheep"
print(len(S))
print(S.find('e'))
print(S.count("a"))
print(S.replace("Ba Ba ","Ta Ta "))

#Qusetion 3
S=input("Enter the String:")
reverse=S[::-1]

if(S==reverse):
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome")

#Qusetion 4
Name=input("Enter the name:")
Roll_number=int(input("Enter the Roll Number:"))
Marks=int(input("Enter the Marks:"))

print("Name: ",Name)
print("Roll Number: ",Roll_number)
print("Marks: ",Marks)

if(Marks>=90):
    print("Grade Point: 10")
    print("Remark: Outstanding")

elif(Marks>90 and Marks>=80):
    print("Grade Point: 9")
    print("Remark: Very Good")

elif(Marks>80 and Marks>=70):
    print("Grade Point: 8")
    print("Remark: Good")

elif(Marks>70 and Marks>=60):
    print("Grade Point: 7")
    print("Remark: Average")

elif(Marks>60 and Marks>=50):
    print("Grade Point: 6")
    print("Remark: Pass")

elif(Marks<50):
    print("Grade Point: 0")
    print("Remark: Fail")

#Qusetion 5
import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

d=(b*b)-(4*a*c)

if(d==0):
    R1=R2=-b/2*a
    print("Roots are: ",R1," and ",R2)

if(d>0):
    R1=(-b+math.sqrt(d))/(2*a)
    R2=(-b-math.sqrt(d))/(2*a)
    print("Roots are: ",R1," and ",R2)

if(d<0):
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-d)/(2*a)
    
    print("Roots are: ")
    print((real_part)/" + i "(imaginary_part))