''' take an integer as input as a user and check wether the number is divisble is sum of digits or not'''

n=int(input("enter the number:"))
n1=n
s=0
while(n>0):
    d=n%10 
    s+=d
    n=n//10
if n1%s==0:     #n became zero after the loop so we took the n1=n 
    print("divisble by that number")
else:
    print("not divisble")
