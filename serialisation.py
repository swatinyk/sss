import pickle,emp
f=open('emp.txt','wb')
n=int(input("enter no of employees"))

for i in range(n):
    eno=int(input("enter employee no"))
    ename=input("enter employee name")
    esal=int(input("enter employee salary"))
    eaddr=input("enter employee address")
    e=emp.employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
