l=[22,-1,42,65,1,-4,6]

small=99
secsmall=99
for i in range(len(l)):
    if small>l[i]:
        secsmall=small
        small=l[i]
    elif secsmall>l[i] and secsmall>small:
        secsmall=l[i]
    print(secsmall)