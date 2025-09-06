import threading
import random

class BarrierWithSemaphore:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.semaphore = threading.Semaphore(0)  # Initial count of 0 to block threads
        self.count = 0
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            self.count += 1
            if self.count == self.num_threads:
                # Release all threads waiting at the barrier
                for _ in range(self.num_threads):
                    self.semaphore.release()
            else:
                # Wait for the other threads
                self.semaphore.acquire()

# Example usage:

class Seat:

    def __init__(self):
        self.barr = BarrierWithSemaphore(3)
        self.turn_l = threading.Lock()
        self.turn = -1

    def seatD(self):
        #print("dem before acquiring")
        print("DEM")
        self.barr.wait()

    def seatR(self):
        #print("rep before acquiring")
        self.barr.wait()
        print("REP")

seat = Seat()

threads = []
for i in range(30):
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
