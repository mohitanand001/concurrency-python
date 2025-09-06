import threading
from time import time

class Foo:
    def __init__(self):
        self.lock = threading.Lock()
        self.turn = 1


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        
        self.lock.acquire()
        print("came to first inside lock ")
        while self.turn != 1: pass
        printFirst()
        self.turn = 2
        self.lock.release()
        print("lock releasing ")


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock.acquire()
        while self.turn != 2: pass
        self.turn = 3
        printSecond()
        self.lock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.lock.acquire()
        while self.turn != 3: pass
        printThird()
        self.lock.release()



foo = Foo()

def f1(): print("first")
def f2(): print("second")
def f3(): print("third")


t1 = threading.Thread(target=foo.first, args=(f1, ))
t2 = threading.Thread(target=foo.second, args=(f2, ))
t3 = threading.Thread(target=foo.second, args=(f3, ))

threads = [t1, t2, t3]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

#foo.first(f1)
#foo.third(f3)
#foo.second(f2)

