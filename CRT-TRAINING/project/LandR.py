import csv
def regis(self,us,pas,phon,pincode):
    self.us=us
    self.pas=pas
    self.phon=phon
    self.pincode=pincode
    with open('reg.csv','a',newline='') as file:
        s=csv.writer(file)
        s.writerow([self.us,self.pas,self.phon,self.pincode])
def login(Self,us,pas):
    with open('reg.csv','r',newline='') as file:
        read= csv.DictReader(file)
        for row in read:
            if row['us'] == us and row['pas'] == pas:
                return True
    return False