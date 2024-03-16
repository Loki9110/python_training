#creating a list

n=["Bro",12,"los angeles",56,"atlanta",45]

#access and slicing the list

p=n[0:3]
q=n[1:4]
r=n[0:3]
s=n[3:]
ll=n[::-1]
lal=n[0:5:2]

print(p,q,r,s,lal)

# loops accesing

for i in n:
    print(i)
print(p,q,r,s)

i=0
nz=len(n)
while (i<n):
    print(nz[i])
    i=i+1

#append

n.append("new york")
print(n)

#insert :it is used to add at a specific position

n.insert(4,23)  #4 is the position where it need to be inserted
print(n)

#multi dimensional list

n2d=[[12,45],["lol","bro"]]
print(n2d)
#print(n[row],[col])
print(n[0][0])
print(n[1][0])
print(n[0][1])

#updating




