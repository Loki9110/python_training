import csv 
class stud:
    def pr(self):
        self.studetails= open("stud.csv","a",newline="")
        self.data=csv.writer(self.studetails)
        self.data.writerow(["studid","studname"])
    
    def studetails(self):
        studid=input("enter student id:")
        studname = input("enter the student name:")
        print("data has been stored")

stud()
stud.studetails
