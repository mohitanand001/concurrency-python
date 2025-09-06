import threading
import random


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.turn_i = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        #print("waiting fizz", self.i)
        while True:
           self.turn_i.acquire()
           self.turn_i.wait_for(
            lambda: ((self.i % 3==0) and (self.i % 5)) or (self.i == self.n + 1) 
        )
           printFizz()
           self.i+=1
           self.turn_i.notify_all()
           self.turn_i.release()
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        #print("waiting buzz", self.i)
        while True:
           self.turn_i.acquire()
           self.turn_i.wait_for(
            lambda: ((self.i % 5 == 0) and (self.i % 3)) or (self.i == self.n + 1)
        )
           if self.i > self.n:
               return
           printBuzz()
           self.i+=1
           self.turn_i.notify_all()
           self.turn_i.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        #print("waiting fizzbuzz", self.i)
        while True:
          self.turn_i.acquire()
          self.turn_i.wait_for(
            lambda: ((self.i % 5 == 0) and
            (self.i % 3 == 0)) or (
                self.i == self.n + 1
            )
        )
          if self.i > self.n:
              return
          printFizzBuzz()
          self.i+=1
          self.turn_i.notify_all()
          self.turn_i.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(1, self.n + 1):
            print("waiting number", self.i)
            self.turn_i.acquire()
            self.turn_i.wait_for(
                lambda: ((self.i % 5 != 0) and
                (self.i % 3 != 0)) or (self.i == self.n+1)
            )
            if self.i > self.n:
                return
            printNumber(self.i)
            self.i+=1
            self.turn_i.notify_all()
            self.turn_i.release()        


f = FizzBuzz(1)

def pfizz(): print("fizz", flush=True)
def pbuzz(): print("buzz", flush=True)
def pfizzbuzz(): print("fizzbuzz", flush=True)
def pnumber(x): print(x, flush=True)


ts = [threading.Thread(target=f.fizz, args=(pfizz, )), 
     threading.Thread(target=f.buzz, args=(pbuzz, )),
     threading.Thread(target=f.fizzbuzz, args=(pfizzbuzz,)),
     threading.Thread(target=f.number, args=(pnumber, ))]

random.shuffle(ts)


for t in ts:
    t.start()

for t in ts:
    t.join()


