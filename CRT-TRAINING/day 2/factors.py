'''take a num input from the user check if the sum of factors of that number is greater than the original number or not 
if yes print yes'''

n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("greater")
else:
    print("nope")
