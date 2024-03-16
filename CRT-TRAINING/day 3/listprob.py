list=[12,42,23,96,7,18,10,133]
min=list[0]
max=list[0]
minid=0
maxid=0
for i in range(len(list)):
     if min>list[i]:
          min=list[i]
          minid=i
     if max<list[i]:
          max=list[i]
          maxid=i
s=min+max
d=max-min
list[minid]=d
list[maxid]=s

          

