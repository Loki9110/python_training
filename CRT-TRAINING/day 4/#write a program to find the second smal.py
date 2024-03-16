#write a program  to find the second smallest negative number from the list

l=[22,-1,42,65,1,-4,6]

small=l[0]
secsmall=l[0]
for i in range(len(l)):
    if small>l[i]:
        small=l[i]
for i in range(len(l)):
    if l[i]>small and l[i]<secsmall:
        secsmall=l[i]
        print(secsmall)
       