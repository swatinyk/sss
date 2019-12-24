import pickle
f=open('emp.txt','rb')

while True:
    try:
       obj=pickle.load(f)
       if(obj.ename=='swati'):
           print("found")
           obj.display()

    except EOFError:
        print("file completed")
        break



