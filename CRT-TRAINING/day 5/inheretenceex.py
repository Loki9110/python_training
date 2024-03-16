'''create a class of name placements which a function info  which displays we have "we have 650 placemments and still counting
    create another class name department with function display which will display the names of the departments present in the college.
    create a class pragati with a function welcome  which displays the message welcome to the pragati enginnering college we are glad
      to have u on board and this pragati class should also display the details about departments and placements'''

class placements:
    def info(self):
        print("pragati engineeri g college has a placements of 650 and still counting")

class department(placements):
    def display(self):
        print("the departments that are available in our institution are:")
        print("cse , mech , civil , ece , eee , ds , aiml")
class pragati(department):
    def welcome(self):
        print("welcome to the pragati engineering college we are glad to have you on board ,have a bright future ahead")

pec=placements()
pec.info()
pec.display()
pec.welcome()

