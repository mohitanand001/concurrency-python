import threading
import random

class H2O:
    def __init__(self):
        self.h_c = 0
        self.o_c = 0
        self.turn_l = threading.Condition()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.turn_l.acquire()
        self.turn_l.wait_for(
            lambda: (self.h_c <= 1 and self.o_c <= 1)
        )
        self.h_c+=1
        releaseHydrogen()
        if self.h_c + self.o_c == 3:
            self.h_c = 0
            self.o_c = 0
        self.turn_l.notify_all()
        self.turn_l.release()
        # releaseHydrogen() outputs "H". Do not change or remove this line.


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.turn_l.acquire()
        self.turn_l.wait_for(
            lambda: self.h_c <= 2 and self.o_c == 0
        )
        releaseOxygen()
        self.o_c+=1
        if self.h_c + self.o_c == 3:
            self.h_c = 0
            self.o_c = 0

        self.turn_l.notify_all()
        self.turn_l.release()

h20 = H2O()

def rH():
    print("H", flush=True)

def rO():
    print("O", flush=True)


n = 20
ts = [threading.Thread(target=h20.hydrogen, args=(rH, )) for i in range(n)]
ts.extend([threading.Thread(target=h20.oxygen, args=(rO, )) for i in range(n)])

random.shuffle(ts)

for t in ts:
    t.start()

for t in ts:
    t.join()
