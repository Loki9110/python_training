n=1441
n1=n
n2=0
while (n>0):
    d=n%10
    n2=n2*10
    n2=n2+d
    n=n//10
if n1==n2:
    print("its a palindrome")
else:
    print("not a palidrome")

