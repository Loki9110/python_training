#write a program in which you take an integer input from the user if it is divisible by 3 and 6 print good number if the integer is divisible by 2 and 7 then print an average number
 #,if the integer is divisble by 4 and 9 its an awesome number else print bad number

n=int(input("enter you number:"))

if n%3==0 and n%6==0:
    print("it is good number")
elif n%2==0 and n%7==0:
    print("it is an average number:")
elif n%4==0 or n%9==0:
    print("it is a awesome number")
else:
    print("bad number")