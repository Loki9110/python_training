#shift all the zereos to the right with out changing order of the remaining numbers
l=[2,0,1024,0,40,230,0]
l1=[0]
count=0
for i in range(len(l)):
    if l[i]!=0:
        l1+=l[i]
for i in range(len(l)):
    if l[i]==0:
        l1+=l[i]
print(l1)

