import threading
import random


# Example usage:

class Seat:

    def __init__(self):
        self.barr = threading.Barrier(3)
        self.turnd = threading.Semaphore(3)
        self.turnr = threading.Semaphore(3)
        self.td = threading.Lock()
        self.tr = threading.Lock()
        self.tr.acquire()


    def seatD(self):
        self.td.acquire()
        self.turnd.acquire()
        self.barr.wait()
        print("DEM", flush=True)
        self.turnd.release()
        self.tr.release()
  
    def seatR(self):
        self.tr.acquire()
        self.turnr.acquire()
        #print("rep acquire")
        self.barr.wait()
        print("REP", flush=True)
        self.turnr.release()
        self.td.release()

seat = Seat()

threads = []
for i in range(32):
    threads.append(threading.Thread(target=seat.seatR))
    threads.append(threading.Thread(target=seat.seatD))


random.shuffle(threads)

for t in threads:
    t.start()


for t in threads:
    t.join()

