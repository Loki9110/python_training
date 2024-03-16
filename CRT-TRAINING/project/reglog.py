import csv
class reglog:

    def reg(self):
        print("registering for ecommerece website")
        usr=input("enter the user name of your choice:")
        pasr=input("enter the  password:")
        self.usr=usr
        self.pasr=pasr
        print("you have successfully registered for this website")

    def db(self):
        with open('reg.csv','a',newline="") as file:
            w=csv.writer(file)
            w.writerow([self.usr,self.pasr])
    def login(self):
        print("please enter your login username and password to continue")
        us=input("enter the username:")
        pas=input("enter the password:")
        self.us=us 
        self.pas=pas
        if us == self.usr and pas == self.pasr:
            print("successful login")
        
        elif us!=self.usr and pas==self.pasr:
            print("enter the correct username")
            self.login()
        elif us==self.usr and pas!=self.pasr:
            print("please enter the correct password")
            self.login()
        else:
            print("please enter the correct credentials")
            self.login()


regi=reglog()
regi.reg()
regi.login()
regi.db()


        
    

