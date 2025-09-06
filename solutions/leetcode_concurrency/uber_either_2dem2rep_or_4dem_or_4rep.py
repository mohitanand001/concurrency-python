# no majority dem or rep
# either 
#1. 2dem + 2rep
#2. 4 dem
#3. 4 rep


import threading
import random

class DemRep:

    def __init__(self):
        self.turn = None
        self.turn_lock = threading.Condition()
        self.demcnt = 0
        self.repcnt = 0

    def dem(self):
        with self.turn_lock:
            self.turn_lock.wait_for(
                    lambda: 
                            (self.demcnt <= 1 and self.repcnt <= 1) or\
                            (self.repcnt == 0) or\
                            (self.repcnt == 2)
                        )
            print("DEM")
            self.demcnt +=1
            if self.demcnt + self.repcnt == 4:
                self.demcnt = 0
                self.repcnt = 0

            self.turn_lock.notify_all()


    def rep(self):
        with self.turn_lock:
            self.turn_lock.wait_for(
                    lambda: (self.repcnt <= 1 and self.demcnt <= 1) or\
                            (self.demcnt == 0) or\
                            (self.demcnt == 2)
                            )
            print("REP")
            self.repcnt+=1
            if self.repcnt + self.demcnt == 4:
                self.repcnt = 0
                self.demcnt = 0

            self.turn_lock.notify_all()


dr = DemRep()

N = 20

ts = [threading.Thread(target=dr.dem) for i in range(N)]
ts.extend(
        [threading.Thread(target=dr.rep) for i in range(N)]
        )

random.shuffle(ts)

[t.start() for t in ts]
[t.join() for t in ts]
