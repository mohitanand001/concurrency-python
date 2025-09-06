#inside bathroom either 3 dems or 3 reps can go
import threading
import random

class Seat:

    def __init__(self):
        self.turn = None
        self.count = 0
        self.turn_lock = threading.Condition()

    def seatD(self):
        with self.turn_lock:

            self.turn_lock.wait_for(
                    lambda: self.turn is None or
                    self.turn == "DEM")

            self.turn = "DEM"
            print("DEM")
            self.count +=1
            if self.count == 3:
                self.count = 0
                self.turn = None

            self.turn_lock.notify_all()

    def seatR(self):
        
        with self.turn_lock:

            self.turn_lock.wait_for(
                    lambda: self.turn is None or\
                            self.turn == "REP")

            self.turn = "REP"
            print("REP")
            self.count +=1
            if self.count == 3:
                self.count = 0
                self.turn  = None
            self.turn_lock.notify_all()



N = 21
s = Seat()
ts= [threading.Thread(target=s.seatD) for i in range(N)]
ts.extend(
    [threading.Thread(target=s.seatR) for i in range(N)]
        )

random.shuffle(ts)

[t.start() for t in ts]
[t.join()  for t in ts]


