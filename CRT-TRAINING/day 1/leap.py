'''check if a give year is leap year or not 
if the year is divisible by 4 and not divisible by 100 or if it is divisible by  400 then it is calld leap year'''

year=int(input("enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
            print("the year is leap year")
else:
    print("not a leap year")
    