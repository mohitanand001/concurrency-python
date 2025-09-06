import threading
import random


# Example usage:

class Seat:

    def __init__(self):
        self.barr = threading.Barrier(4)
        self.turnd = threading.Semaphore(2)
        self.turnr = threading.Semaphore(2)


    def seatD(self):
        self.turnd.acquire()
        self.barr.wait()
        print("DEM", flush=True)
        self.turnd.release()
  
    def seatR(self):
        #print("rep before acquiring")
        self.turnr.acquire()
        #print("rep acquire")
        self.barr.wait()
        print("REP", flush=True)
        self.turnr.release()

seat = Seat()

threads = []
for i in range(32):
    val = int ((random.random()*1000)%2)
    #print(val)
    if val == 1:
        func=seat.seatD
    else:
        func= seat.seatR
    threads.append(threading.Thread(target=func))


for t in threads:
    t.start()


for t in threads:
    t.join()

