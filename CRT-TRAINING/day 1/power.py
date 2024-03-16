#write a program to accept 2 inputs from user in the float format then convert into integer datatype and  calculate a^b

a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
a=int(a)
b=int(b)
res=a**b
print("result is:",res)