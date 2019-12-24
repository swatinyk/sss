class person:
    def __init__(self):
        self.name='durga'
        self.dob=self.DOB()

    def display(self):
        print("name is:",self.name)

    class DOB:
        def __init__(self):
            self.db=25
            self.mm='june'
            self.yy=777
        def display(self):
            print("dob: {}/{}/{} :".format(self.db,self.mm,self.yy))

p=person()
p.display()
person().DOB().display()
p.dob.display()
