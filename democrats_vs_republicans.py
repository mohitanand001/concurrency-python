import threading
import random
import time

class Seat:

    def __init__(self):
        self.dem_or_rep = threading.Condition()
        self.count = 0
        self.turn = -1

    def seatdem(self):
        print("trying dem")
        self.dem_or_rep.acquire()
        print("entered dem")
        if self.turn == -1:
            self.turn = 0
        
        while self.turn != 0:
            #time.sleep(0.25)
            print("waiting dem")
            self.dem_or_rep.wait()

        self.count+=1

        print("DEM")
        if self.count == 3:
            self.count = 0
            self.turn = -1
            print("==========")


        self.dem_or_rep.notify_all()
        self.dem_or_rep.release()

    def seatrep(self):
        print("trying rep") 

        self.dem_or_rep.acquire()
        print("entering rep")

        if self.turn == -1:
            self.turn = 1

        while self.turn != 1:
            #time.sleep(0.25)
            print("waiting rep")
            self.dem_or_rep.wait()

        self.count+=1

        print("REP")
        if self.count == 3:
            self.count = 0
            self.turn = -1
            print("==========")


        self.dem_or_rep.notify_all()
        self.dem_or_rep.release()




seat = Seat()

#t1 = threading.Thread(seat.seatdem)
#t2 = threading.Thread(seat.seatrep)
#t3 = threading.Thread(seat.seatrep)


threads = []
for i in range(30):
    val = int ((random.random()*1000)%2)
    #print(val)
    if val == 1:
        func=seat.seatdem
    else:
        func= seat.seatrep
    threads.append(threading.Thread(target=func))


for t in threads:
    t.start()


for t in threads:
    t.join()


