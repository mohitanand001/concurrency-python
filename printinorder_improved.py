import threading

class Foo:
    def __init__(self):
        self.condition = threading.Condition()
        self.turn = 1  # To control the order of execution
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.condition:
            print("came to first inside lock")
            while self.turn != 1:
                self.condition.wait()  # Efficient wait instead of busy-waiting
            printFirst()
            self.turn = 2
            self.condition.notify_all()  # Notify other threads that they can proceed
    
    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition:
            while self.turn != 2:
                self.condition.wait()  # Efficient wait
            printSecond()
            self.turn = 3
            self.condition.notify_all()  # Notify other threads that they can proceed
    
    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.condition:
            while self.turn != 3:
                self.condition.wait()  # Efficient wait
            printThird()

foo = Foo()

def f1(): print("first")
def f2(): print("second")
def f3(): print("third")

# Create threads
t1 = threading.Thread(target=foo.first, args=(f1,))
t2 = threading.Thread(target=foo.second, args=(f2,))
t3 = threading.Thread(target=foo.third, args=(f3,))

# Start threads (changing the order of t2 and t3)
threads = [t3, t2, t1]
for thread in threads:
    thread.start()

# Wait for threads to finish
for thread in threads:
    thread.join()

