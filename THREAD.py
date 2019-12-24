from  threading import *
def disply():
    print("name of child thread ",current_thread().getName())

Thread(target=disply).start()

disply()
print("name of parent  thread ",current_thread().getName())
