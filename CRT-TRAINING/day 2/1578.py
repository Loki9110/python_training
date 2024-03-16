n=int(input("enter the number:"))
nod=0
n1=n
sod=0
while (n>0):
    nod=nod+1
    n=n//10
while (n1>0):
    dig=n1%10
    sod=sod+(dig**nod)
    nod=nod-1
    n1=n1//10
print(sod)


    
