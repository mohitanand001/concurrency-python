import threading
import time

def f1(): 
    time.sleep(10); 
    
    print("hello after 10 seconds")

t1 = threading.Thread(target=f1)
t1.start()
t1.join()
