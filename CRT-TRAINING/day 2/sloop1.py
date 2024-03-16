n=int(input("enter the number:")) 
sum=0
count=0
mul=0
while(n>0):
    count=count+1
    digit=n%10
    sum=sum+digit
    mul=mul*digit
    print(digit)
    n=n//10
print(mul)
print(sum)
print(count)