'''write a program to check the type of triangle where you take the input from the user for threes sides and classify 
it accordingly into equilatoral ,isosceles and scalene'''

x=int(input("enter the first side of the triangle:"))
y=int(input("enter the second side of the triangle:"))
z=int(input("enter the third side of the triangle:"))

if x==y==z:
    print("it is an equilatoral traingle")
elif x==y or y==z or x==z:
    print("it is a isosceles traingle")
else:
    print("it is a scalene triangle")