#create a dictionary with atleas 4 key value pairs 


dict={1:"tokyo",2:"rio",3:"rotterdam",4:"mersaille"}

print(dict)
#accesing your values using keys

n=dict[2]
print(n)

o=dict[4]
print(o)

#accessing the whole dic using loops

for i in dict:
    print(i,dict[i])
#try to add duplicates
dict[5]="glasgow"
print(dict)
#try to remove a value from a dictionary   
dict.remove[4]
print(dict)


