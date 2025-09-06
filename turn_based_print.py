import threading
import random


class Print:

    def __init__(self):

        self.turna = threading.Lock()
        self.turnb = threading.Lock()
        self.turnb.acquire()

    def f1(self):
        self.turna.acquire() 
        print("f1")
        self.turnb.release()


    def f2(self):
        self.turnb.acquire()
        print("f2")
        self.turna.release()


pri = Print()

threads = []
for i in range(5):
    threads.append(threading.Thread(target=pri.f1))
    threads.append(threading.Thread(target=pri.f2))

random.shuffle(threads)

print(threads)

for t in threads:
    t.start()

for t in threads:
    t.join()
