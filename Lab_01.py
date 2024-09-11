#Question 1
import time
a=int(input("Enter the first no."))
b=int(input("Enter the second no."))

t1=time.time()
print("Sum is: ",a+b)
print("Difference is: ",a-b)
print("Product is: ",a*b)
print("Frcational Quotient is: ",a/b)
print("Integer Quotient is: ",a//b)
print("Remainder is: ",a%b)
print(time.time()-t1)

#Question 2
from math import sqrt,degrees,acos
a=int(input("Enter the length of first side:"))
b=int(input("Enter the length of second side:"))
c=int(input("Enter the length of third side:"))
s=(a+b+c)/2
Area=sqrt(s*(s-a)*(s-b)*(s-c))
A=degrees(acos((b**2+c**2-a**2)/(2*b*c)))
B=degrees(acos((a**2+c**2-b**2)/(2*a*c)))
C=degrees(acos((b**2+a**2-c**2)/(2*b*a)))

print("Perimeter is ",2*s)
print("Area is ",Area)
print("Angle A is: ",A)
print("Angle B is: ",B)
print("Angle C is: ",C)

#Question 3
c = int(input("Enter temperature in celsius: "))
O=(c*1.8)+32
print("Temp in Fahrenheit is: ",O)