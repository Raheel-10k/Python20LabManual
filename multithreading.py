from threading import Thread
from time import sleep
def hi():
    for i in range(10):
        print("Hi")
        sleep(0.5)
def hello():
    for i in range(10):
        print("Hello")
        sleep(0.5)
thread1=Thread(target=hi)
thread2=Thread(target=hello)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("End of execution")