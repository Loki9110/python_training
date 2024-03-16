'''create a class ticket which will be the abstract class inside that create the function book ticket which is the abstract method 
   and has nothing in it . 
    create a class makemytrip which will will use the book ticket function from ticket class to take the details such as name,phone number 
    emailid ,journeydate and display the message saying thank you for booking from makemytrip. 
    
    create a class irctc which will use the bookticket of ticket class and takes the same details as makemytrip but in the end 
     it will give an option to the user to select wether it is one way or round trip if the user option is round trip it again asks the
     user to enter the return date as well and then print the message thank you for choosing irctc 
     else
     it prints thank you choosing irctc
     
     create a class indigo which takes the details as a irctc and just asks which mode of transport you want to go in and 
     displays thank you for choosing indigo'''


from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass

class makemytrip(ticket):
    def bookticket(self):
        n=input("enter your name:")
        ph=int(input("enter your phone number:"))
        mail=input("enter your emailid:")
        jd=input("enter your journey date:")
        print("THANK YOU FOR BOOKING FROM MAKEMYTRIP")

class irctc(ticket):                            #doubt
    def bookticket(self):
        n=input("enter your name:")
        ph=int(input("enter your phone number:"))
        mail=input("enter your emailid:")
        jd=input("enter your journey date:")
        print("enter wether it is one way or two way")
        l=input("1.oneway/t2.round")
        l.lower()
        if l =="round" or l=="2":
            r=input("enter the return date:")
            print("thank you fro choosing irctc")
        else:
            print("enter the return date")
class indigo(ticket):
    def bookticket(self):
        n=input("enter your name:")
        ph=int(input("enter your phone number:"))
        mail=input("enter your emailid:")
        jd=input("enter your journey date:")
        print("enter wether it is one way or two way")
        l=input("1.oneway/t2.round")
        l.lower()
        if l =="round" or l=="2":
            r=input("enter the return date:")
            print("enter the mode of transport")
            mod=input("1.flight/t2.railways/t3.bus")
            print("thank you fro choosing indigo")
        else:
            mod=input("1.flight/t2.railways/t3.bus")
            print("thanking you fro choosing indigo")


myt1=makemytrip()
myt2=irctc()
myt3=indigo()
myt1.bookticket()
myt2.bookticket()
myt3.bookticket()

   




            
