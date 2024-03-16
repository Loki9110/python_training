'''create an ATM system 

    the first task will be displaying the remaining amount in atm in 
    the following options
    1.rupay
    2.visa
    3.master card
    authentication of user (username and password should be equal)
    if the user is authenticated cgive him the following options to choose
    !. check balance 
    2.  cash withdrawal(automatic balance display)  based on card the withdrawal limit is 2000,5000,8499
    3.  cash deposit  (automatic balance dispaly)
    4. mini statement of the last 3 transactions
     card renewal 
'''

class auth:
    def at(self):
        amount=int(input("enter the amount in you bank account"))
        self.amount=amount
        print("select the card of your choice")
        c=input("1.rupay\t2.visa\t3.mastercard")
        name=input("enter your name:")
        pas=input("enter your password")
        self.name=name
        self.pas=pas
        if name == pas:
            print("authentication successfull")
        else:
            print("authentication not successful")
            self.at()
    def display(self):
        self.at()
        if self.name == self.pas:
            print("choose the task you want to do")
            t=input("1.check balance\t2.cash withdrawal\t3.cash deposit\t4.mini statement")
            if t == "check balance" or t == "1":
                self.checkbal
                
            elif t == "cash withdrawal" or t == "2":
                self.cashdraw()
                
            elif t == "cash deposit" or t == "3":
                self.depo()
                
            elif t == "cash withdrawal" or t == "2":
                self.draw()
                
            elif t == "mini statement" or t == "3":
                self.mini()
                
            else:
                print("you should select 1 option")
                self.display()
    def checkbal(self):
        print("the amount of balance in your bank accout:",self.amount)

    def cashdraw(self):
        drawcash=(int(input("enter the amount of cash you want to withdraw:")))
        if self.c == "1" or self.c =="rupay" and drawcash <= 2000:
            rem=self.amount - drawcash
            print("enter the remaining amount:")

        pass
    def depo(self):
        pass
    def mini(self):
        pass

        
        


        
        