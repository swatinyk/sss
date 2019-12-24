from threading import *
import queue
e=queue.Queue()
e.put('10')
e.put('20')
e.put('30')
while not e.empty():
    print(e.get())



'''def producer():
       while True:


        randomno=random.randint(1,10)

        e.put(randomno)
        print("producer producing items",randomno,"and notifying consumer")
        time.sleep(5)

def consumer():
       while True:

        print("waiting for producer to produce ")

        print(" production started",e.get())

        time.sleep(5)
t1=Thread(target=consumer)
t2=Thread(target=producer)
t1.start()
t2.start()
#time.sleep(8)
#print(t1.isAlive())
#print(t2.isAlive())'''
