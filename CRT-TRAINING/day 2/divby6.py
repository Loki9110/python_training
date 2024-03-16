'''calculate the difference  of sum of numbers that are divisible by 6 and numbers not divisible by 6 in the range of first 30 numbers'''

s1=0
s2=0

for i in range(0,30):
    if i%6==0:
        s1+=i
    else:
        s2+=i
print(abs(s1-s2))
