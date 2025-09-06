import threading
import time

def f1():
   time.sleep(20)
   print("hello after 20 seconds")

t1 = threading.Thread(target=f1)
t1.start()

