#create a classf15 with functions as lights,fan and ac
#lights :when it is called it prints the colour of light whic is taken as parameter to the func
#fan:when it called it displays reg which it is taken as parameter for func
#ac displays curr room temp and the out side temp which are taken as parameters
#write a 4th function which is display which displays the difference in outside tempereture and room temperature of ac and it displays the fan speed


class f15:
    def __init__(self,st,en) -> None:   # this function is a constructor
        print("ds and it students  are currently learning python")
        ds=74
        it=75
        tot=ds+it
        print("the total students are",tot)
        print("the start time of the class is",st,"and the end time of the class is:",en)

    def lights(self,c):
        print("the color of the fan is:",c)
    def fan(self,r):
        self.r=r
        print("the sped of the fan is:",r)
    def ac(self,t,ot):
        self.t=t
        self.ot=ot
        print("the current temperature is:",t,"and the outside temperature is:",ot)
    def display(self):
        print(self.ot-self.t)
        print(self.r)
loki=f15(9,4)     # object name = class name
loki.lights("neon")
loki.fan(4)
loki.ac(23,30)
loki.display()


#constructor is a function is autoamtically executed ehenever the object is created allocates memory as soon as object is created