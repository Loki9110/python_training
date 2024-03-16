#car showroom project
'''in show room there are only 3 car companies toyota,mahindra,mercedes   
 take the input from the user for the car company name and in the input message give the option of three companies
 this userr input company name goes as the input/argument to model name function ,which welcomes the user accordingly 
 to the company  name. in the first function  ask the user to enter the specific model name for that company

 in second function whose name is variant. according to the car company name and car model the user should be asked to 
  enter the variant he would likes to choose from petrol and diesel 

  in the last  display function according to the car company ,car model name and car variant first its ex show room 
   price should be displayed and then its on road price should be displayed , which is calculated as 
   ex showroom price+gst+sgst+insurance.the sgst ,cgst and the insurance have a comman value throughtout the car showroom  
 
'''

class showroom:

    def __innit__(self):
        print("welcome to the infinity showroom")
    def name(self):
        print("tell us the car brand you're interested in")
        car=input("interested car brand is:")
        if car == "toyota":
            print("welcome the toyota fam")
            mod=input("toyota model you are interested in:")
            self.variant(car,mod)
        elif car == "mahindra":
            print("welcome the mahindra fam")
            mod=input("mahindra model you are interested in:")
            self.variant(car,mod)
        elif car == "mercedes":
            print("welcome the mercedes fam")
            mod=input("mercedes model you are interested in:")
            self.variant(car,mod)   
        else:
            print("the brand you like isnt available here")

    def variant(self,car,mod):
        if car =="toyota" and mod=="innova":
            var=input("enter the variant you are interested in:")
        elif car =="toyota" and mod=="supra":
            var=input("enter the variant you are interested in:")
        elif car =="toyota" and mod=="corolla":
            var=input("enter the variant you are interested in:")
        elif car =="mahindra" and mod=="thar":
            var=input("enter the variant you are interested in:")
        elif car =="mahindra" and mod=="scorpio":
            var=input("enter the variant you are interested in:")
        elif car =="toyota" and mod=="sumo":
            var=input("enter the variant you are interested in:")
        elif car =="mercedes" and mod=="g-class":
            var=input("enter the variant you are interested in:") 
        elif car =="mercedes" and mod=="e-class":
            var=input("enter the variant you are interested in:")
        elif car =="mercedes" and mod=="amg":
            var=input("enter the variant you are interested in:")

    def display(self,car,mod,var):
        insurance=2000
        gst=2000
        sgst=2000
        if car=="toyota" and mod=="innova" and var=="petrol":
            price=1200000
            overall_price=price+insurance+gst+sgst
        elif car=="toyota" and mod=="innova" and var=="diesel":
            price=1300000
            overall_price=price+insurance+gst+sgst
        elif car=="toyota" and mod=="supra" and var=="petrol":
            price=7500000
            overall_price=price+insurance+gst+sgst
        elif car=="toyota" and mod=="supra" and var=="diesel":
            price=8000000
            overall_price=price+insurance+gst+sgst
        elif car=="toyota" and mod=="corolla" and var=="petrol":
            price=600000
            overall_price=price+insurance+gst+sgst
        elif car=="toyota" and mod=="corolla" and var=="diesel":
            price=1200000
            overall_price=price+insurance+gst+sgst
        elif car=="mahindra" and mod=="thar" and var=="petrol":
            price=1200000
            overall_price=price+insurance+gst+sgst
        elif car=="mahindra" and mod=="thar" and var=="diesel":
            price=1400000
            overall_price=price+insurance+gst+sgst
        elif car=="mahindra" and mod=="scorpio" and var=="petrol":
            price=1300000
            overall_price=price+insurance+gst+sgst
        elif car=="mahindra" and mod=="scorpio" and var=="diesel":
            price=1400000
            overall_price=price+insurance+gst+sgst
        elif car=="mahindra" and mod=="sumo" and var=="petrol":
            price=1000000
            overall_price=price+insurance+gst+sgst
        elif car=="mahindra" and mod=="sumo" and var=="diesel":
            price=1200000
            overall_price=price+insurance+gst+sgst
        elif car=="mercedes" and mod=="g-class" and var=="petrol":
            price=1200000
            overall_price=price+insurance+gst+sgst



          

                                         

        
        
              