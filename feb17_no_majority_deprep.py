#Imagine at the end of a political conference, republicans and democrats are trying to leave the venue and ordering Uber rides at the same time. However, to make sure no fight breaks out in an Uber ride, the software developers at Uber come up with an algorithm whereby either an Uber ride can have all democrats or republicans or two Democrats and two Republicans. All other combinations can result in a fist-fight.




import threading
import random



class Seat:

    def __init__(self):
        self.dcnt = 0
        self.rcnt = 0
        self.turn_l = threading.Condition()

    def seatD(self):
        
        self.turn_l.acquire()
        #print("waitin for cond dem", self.turn_l)
        self.turn_l.wait_for(lambda: (self.dcnt == 1 and self.rcnt==2) or (self.rcnt==0) or (self.rcnt == 1 and self.dcnt < 2))
        self.turn = "DEM"
        self.dcnt+=1
        print("DEM")
        if self.dcnt + self.rcnt== 4:
            self.dcnt = 0
            self.rcnt = 0
        self.turn_l.notify_all()
        self.turn_l.release()


    def seatR(self):
        self.turn_l.acquire()
        #print("waiting for cond rep", self.turn_l)
        self.turn_l.wait_for(lambda: (self.rcnt == 1 and self.dcnt==2) or (self.dcnt==0 ) or (self.dcnt == 1 and self.rcnt < 2) )
        self.rcnt+=1
        print("REP")
        if self.dcnt + self.rcnt == 4:
            self.dcnt = 0
            self.rcnt = 0
        self.turn_l.notify_all()
        self.turn_l.release()

s = Seat()

n = 24
ts = [threading.Thread(target=s.seatD) for i in range(n)]
ts.extend( [threading.Thread(target=s.seatR) for i in range(n)])
random.shuffle(ts)

for t in ts:
    t.start()

for t in ts:
    t.join()
