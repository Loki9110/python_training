'''write a program to check the onroad price of a bike under the conditions if the price is greater than 72000 then the income tax is 10% of the original price and insurnce s=is 15% of the actual price 
if the price is greater than 150000 and less than 200000 the tax would be 25% and the insurance will be 20%
if the price is above 200000 then  taax wll be 35% and the insurance will be 28%
otherwise minimum price starts with 75000 enter a proper price
onroad price= tax + insurance'''


price = int(input("enter the price of the bike:₹"))

if price>72000 and price<150000:
    tax=price*(10/100)
    insur=price*(15/100)
    onroad= tax+insur+price
    print("the onroad price is:₹",int(onroad))
elif price>150000 and price<200000:
    tax=price*(25/100)
    insur=price*(20/100)
    onroad= tax+insur+price
    print("the onroad price is:₹",int(onroad))
elif price>200000:
    tax=price*(35/100)
    insur=price*(28/100)
    onroad= tax+insur+price
    print("the onroad price is:₹",int(onroad))
else:
    print("enter the proper price")
