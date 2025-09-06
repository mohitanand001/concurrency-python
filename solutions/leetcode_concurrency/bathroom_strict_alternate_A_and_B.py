

import threading
import random

class AB:

    def __init__(self):
        self.turn = None
        self.turn_lock = threading.Condition()


    def A(self):
        with self.turn_lock:
            self.turn_lock.wait_for(
                    lambda: self.turn is None or \
                            self.turn == "A")
            print("A")
            self.turn = "B"
            self.turn_lock.notify_all()

    def B(self):
        with self.turn_lock:
            self.turn_lock.wait_for(
                    lambda: self.turn is None or \
                            self.turn == "B")
            print("B")
            self.turn = "A"
            self.turn_lock.notify_all()

N = 21

ab = AB()

ts = [threading.Thread(target=ab.A) for i in range(N)]
ts.extend(
        threading.Thread(target=ab.B) for i in range(N)
        )

random.shuffle(ts)

[t.start() for t in ts]
[t.join() for t in ts]

