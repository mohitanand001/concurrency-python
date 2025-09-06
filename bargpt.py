import threading
import random

class Seat:
    def __init__(self):
        self.barr = threading.Barrier(3)  # Barrier for 3 threads
        self.turn_l = threading.RLock()

    def seatD(self):
        print("dem before acquiring")
        self.turn_l.acquire()
        self.barr.wait()  # Wait for 3 threads
        print("DEM")
        self.turn_l.release()

    def seatR(self):
        print("rep before acquiring")
        self.turn_l.acquire()
        self.barr.wait()  # Wait for 3 threads
        print("REP")
        self.turn_l.release()

seat = Seat()

threads = []
for i in range(30):
    val = int((random.random() * 1000) % 2)
    if val == 1:
        func = seat.seatD
    else:
        func = seat.seatR
    threads.append(threading.Thread(target=func))

# Start all threads
for t in threads:
    t.start()

# Join all threads (wait for them to complete)
for t in threads:
    t.join()

