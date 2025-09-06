import threading
import random



class Seat:

    def __init__(self):
        self.turn = None
        self.cnt = 0
        self.turn_l = threading.Condition()

    def seatD(self):
        
        self.turn_l.acquire()
        #print("waitin for cond dem", self.turn_l)
        self.turn_l.wait_for(lambda: self.turn is None or self.turn == "DEM")
        self.turn = "DEM"
        self.cnt+=1
        print("DEM")
        if self.cnt == 3:
            self.cnt = 0
            self.turn = None
        self.turn_l.notify_all()
        self.turn_l.release()


    def seatR(self):
        self.turn_l.acquire()
        #print("waiting for cond rep", self.turn_l)
        self.turn_l.wait_for(lambda: self.turn is None or self.turn == "REP")
        self.cnt+=1
        self.turn = "REP"
        print("REP")
        if self.cnt == 3:
            self.cnt = 0
            self.turn = None
        self.turn_l.notify_all()
        self.turn_l.release()

s = Seat()

n = 21
ts = [threading.Thread(target=s.seatD) for i in range(n)]
ts.extend( [threading.Thread(target=s.seatR) for i in range(n)])
random.shuffle(ts)

for t in ts:
    t.start()

for t in ts:
    t.join()
