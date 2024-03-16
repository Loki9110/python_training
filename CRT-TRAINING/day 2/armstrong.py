n=int(input("enter the number:"))
nod=0
n1=n
sod=0
org=n1
while (n>0):    #for finding the digits
    nod=nod+1
    n=n//10
while (n1>0):
    dig=n1%10       # 153= 1^3+5^3+3^3
    sod=sod+(dig**nod)
    n1=n1//10
if sod==org:
    print("armstrong number") 
else:
    print("not an armstrong number")


    
