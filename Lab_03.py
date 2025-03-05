#Question 1
n=int(input("Enter the number:"))
for i in range(1,n+1,1):
    print(i,"->",i**2)

#Question 2
n=int(input("Enter the number:"))
org=n
sum=0
while(n!=0):
    digit=n%10
    sum+=digit
    n=int(n/10)
print("Number -> ",org," Sum of digits->",sum)

#Question 3
n=int(input("Enter the number of terms for fibonacci series:"))
t1=0
t2=1
print(t1)
print(t2)
i=2
while(i!=n):
    nextTerm=t1+t2
    print(nextTerm)
    t1=t2
    t2=nextTerm
    i=i+1

#Question 4
n=int(input("Enter the number for which you want table: "))
limit=int(input("Enter the length of table: "))
for i in range(1,limit+1,1):
    print(n*i)

#Question 5
str=input("Enter the string:")
is_alphanumeric=True
for i in str:
    if(not i.isalnum()):
        is_aplhanumeric=False
if(is_aplhanumeric):
    print("True")
else:
    print("False")



#Question 6
str=input("Enter the string:")
char=input("Enter the character whose occurrence you want to know")
count=0
for i in range(len(str)):
    if(str[i]==char):
        count=count+1
print("Total occurences ->",count)
    
