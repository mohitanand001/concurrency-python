import threading
import random

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.turn = 0
        self.value = 0 
        self.turn_l = threading.Condition()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(self.n):
            self.turn_l.acquire()
            self.turn_l.wait_for(lambda: self.turn == 0)
            printNumber(0)
            self.turn = (1 if i % 2 == 0 else 2)
            self.value+=1
            self.turn_l.notify_all()
            self.turn_l.release()

        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n//2):
            self.turn_l.acquire()
            self.turn_l.wait_for(lambda: self.turn == 1)
            printNumber(self.value)
            self.turn = 0
            self.turn_l.notify_all()
            self.turn_l.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n//2):
            self.turn_l.acquire()
            self.turn_l.wait_for(lambda: self.turn == 2)
            printNumber(self.value)
            self.turn = 0
            self.turn_l.notify_all()
            self.turn_l.release()
        

def printNumber(x):
    print(x, flush=True)
        
z = ZeroEvenOdd(2)
ts = []
ts.append( threading.Thread(target=z.zero, args=(printNumber,)  ) )
ts.append(threading.Thread(target=z.even, args=(printNumber,)) )
ts.append(threading.Thread(target=z.odd, args=(printNumber,)))

random.shuffle(ts)

for t in ts:
    t.start()


for t in ts:
    t.join()

