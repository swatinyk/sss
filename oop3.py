class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print("employee no is : ",self.eno)
        print("employee name is : ",self.ename)
        print("employee salary is : ",self.esal)
        print("git commit1")
        print("git commit2")

e=employee(10,'swati',2000)

class test:
    def modify(e):
        e.esal=e.esal+1000
        e.display()



test.modify(e)
