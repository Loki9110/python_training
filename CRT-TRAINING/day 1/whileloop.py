'''calculate the sum of digits of a number which is taken as input from user '''

n=int(input("enter the number:"))
s=0
while n>0:
    s=s+(n%10)
    n=n//10
print(s)  