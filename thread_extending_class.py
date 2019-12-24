from threading import *
import time

print(current_thread().isDaemon())
def child():

    for i in range (5):
           print("i am a child thread")
           time.sleep(2)


p1=Thread(target=child,name="swati")
print(p1.daemon)
p1.setDaemon(True)
print("main thread ends")

