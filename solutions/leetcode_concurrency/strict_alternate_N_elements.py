# N will be given in input, you need to print "A" and "B" strictly alternating 
# in groups of N, 
#ex: N = 2, you will print either AABBAABB...
# or BBAABBAA.. (the number of threads will decide when this sequence ends)

import threading
import random

class ABN:

    def __init__(self, N):
        self.N = N
        self.turn = None
        self.count = 0
        self.turn_lock = threading.Condition()

    def A(self):
        with self.turn_lock:

            self.turn_lock.wait_for(
                    lambda: self.turn is None or \
                            self.turn == "A")
            self.count +=1
            self.turn = "A"
            print("A", end='')
            if self.count == self.N:
                self.turn = "B"
                self.count = 0
            self.turn_lock.notify_all()


    def B(self):
        with self.turn_lock:
            self.turn_lock.wait_for(
                    lambda: self.turn is None or \
                            self.turn == "B")
            self.count +=1
            self.turn = "B"
            print("B", end='')
            if self.count == self.N:
                self.turn = "A"
                self.count = 0
            self.turn_lock.notify_all()





M = 20

ab = ABN(N=4)

ts = [threading.Thread(target=ab.A) for i in range(M)]
ts.extend(
        threading.Thread(target=ab.B) for i in range(M)
        )

random.shuffle(ts)

[t.start() for t in ts]
[t.join() for t in ts]

print()
