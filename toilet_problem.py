import threading
import random
import time



class Toilet:

    def __init__(self):
        pass
        self.turn = None
        self.turn_l = threading.Condition()
        self.count_l = threading.Lock()
        self.count = 0


    def enterM(self, name):
        self.turn_l.acquire()
        self.turn_l.wait_for(lambda:
                self.count >= 0 and self.count <= 2
                )
        self.count+=1
        self.turn_l.notify_all()
        self.turn_l.release()
        
        print(f"{name} entering toilet", self.count)
        time.sleep(0.1)
        print(f"{name} leaving toilet", self.count)

        self.turn_l.acquire();
        self.count-=1
        self.turn_l.notify_all()
        self.turn_l.release()


    def enterF(self, name):
        self.turn_l.acquire()
        self.turn_l.wait_for(lambda:
                self.count <= 0 and self.count >= -2
                )
        self.count-=1
        self.turn_l.notify_all()
        self.turn_l.release()
         
        print(f"{name} entering toilet", self.count)
        time.sleep(0.01)
        print(f"{name} leaving toilet", self.count)

        self.turn_l.acquire();
        self.count+=1
        self.turn_l.notify_all()
        self.turn_l.release()




to = Toilet()

n = 30

ts = [threading.Thread(target=to.enterM, args=("male"+str(i), ) ) for i in range(n)]
ts.extend([threading.Thread(target=to.enterF, args=("female"+str(i), )) for i in range(n)])


random.shuffle(ts)


for t in ts:
    t.start()

for t in ts:
    t.join()
