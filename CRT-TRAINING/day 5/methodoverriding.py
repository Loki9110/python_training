'''run time polymorphism (method overridig)
  
   overriding is possible we cahange the functionality o function as we want because we are inheriting the 
'''
class daddy:
    def ps5(self):
        print("will buy an ps5 pro")

    def pc(self):
        print("normal low end pc")

class son(daddy):
    def pc(self):
        print("need a pc with RTX 4090 gpu, 144 hz monitor and i9 processor for studies ")

buy=son()
buy.ps5()
buy.pc()