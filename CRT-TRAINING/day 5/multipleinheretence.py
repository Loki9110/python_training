class smarks:
    lapde=int(input("enter the marks of lapde"))
    dsa=int(input("enter the marks of dsa"))
    
class pracmarks:
    pracdsa=int(input("enter the marks of pracdsa:"))
class a(smarks,pracmarks):
    def res(self):
        if self.lapde<=40 and self.dsa<=40 and self.pracdsa<=40:
            print("failed the exam")
        else:
            print("passed the exam")
ma=a()
ma.res()