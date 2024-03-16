import csv
f=open("stud.csv","a",newline="")
a= csv.writer(f)
a.writerow(["student","roll","dep"])
studname=input("enter the name of the student:")
roll=input("enter the roll no:")
dep=input("enter the dept:")
a.writerow([studname,roll,dep])
print("records have been saved")