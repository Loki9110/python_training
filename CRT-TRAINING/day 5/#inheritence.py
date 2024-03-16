#inheritence

class faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print("faculty information is :",self.f_name,self.department,self.f_id)
lolz=faculty("loki","ds",34)
lolz.print_info()

class ds(faculty):
    pass
lolz=ds("sri","ds",10)
lolz.print_info()
        