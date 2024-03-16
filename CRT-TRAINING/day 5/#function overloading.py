#function overloading  (compile time polymorphism):same function name but different functionality  example we can do both addition and concatenaton using +
#  3+5=8  and "3"+"5"=35
class arithematic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

addition=arithematic()
addition.add(10)
addition.add(12,13)
addition.add(4,5,6)

#function overloading and constructor overloading doesnt exist in python because it only takes the latesr function written in class it wont the previous functios
