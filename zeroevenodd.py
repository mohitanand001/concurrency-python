import threading
import time
import random


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.curr_l = threading.Condition()
        self.curr = 0
        self.odd_print = 0
        self.val = 0
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        #print("trying inside 0")
        self.curr_l.acquire()
        self.curr_l.wait_for(lambda: self.curr == 0)
        #while(self.curr != 0):
        #    self.curr_l.wait()
        printNumber(0)
        self.curr = 1
        self.odd_print = (self.odd_print ^ 1)
        self.val += 1
        self.curr_l.notify_all()
        self.curr_l.release()
        
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        #print("trying inside even")
        self.curr_l.acquire()
        self.curr_l.wait_for(lambda: self.curr == 1)
        #while(self.curr != 1 and self.odd_print != 1):
        #     self.curr_l.wait()
        
        printNumber(self.val)
        self.curr = 0
        self.curr_l.notify_all()
        self.curr_l.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        #print("trying inside odd")
        self.curr_l.acquire()
        self.curr_l.wait_for(lambda: self.curr == 1)
        #while(self.curr != 1 and self.odd_print != 0):
        #     self.curr_l.wait()
        printNumber(self.val)
        self.curr = 0
        self.curr_l.notify_all()
        self.curr_l.release()
        

def printNumber(x):
    print("value is", x, flush=True)

zer = ZeroEvenOdd(10)
ts = []
for i in range(10):
    ts.append(threading.Thread(target=zer.zero, args=(printNumber, )))
    ts.append(threading.Thread(target=zer.odd, args=(printNumber, )))
    ts.append(threading.Thread(target=zer.even, args=(printNumber, )))


random.shuffle(ts)

for t in ts:
    t.start()

for t in ts:
    t.join()

