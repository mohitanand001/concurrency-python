import threading
import random
import time

class Queue:
    def __init__(self):
        self._elements = []
        self.reader_lock = threading.Lock()
        self.writer_lock = threading.Lock()
        self.reader_cnt = 0
    
    def enque(self, item):
        self.writer_lock.acquire()
        self._elements.append(item)
        print(f"Item enqueued: {item}")
        self.writer_lock.release()
    
    def deque(self):
        self.writer_lock.acquire()
        if len(self._elements) > 0:
            item = self._elements.pop(0)
            print(f"Item dequeued: {item}")
        else:
            print("Queue is empty")
        self.writer_lock.release()
    
    def getleft(self):
        self.reader_lock.acquire()
        self.reader_cnt += 1
        if self.reader_cnt == 1:
            self.writer_lock.acquire()  # acquire writer lock when first reader arrives
        self.reader_lock.release()

        # Non-critical section: readers can do this without issue
        if len(self._elements) > 0:
            print(f"Left element: {self._elements[0]} | Reader count: {self.reader_cnt}")
        else:
            print(f"Empty queue | Reader count: {self.reader_cnt}")
        
        time.sleep(1)  # Simulating reading operation

        self.reader_lock.acquire()
        self.reader_cnt -= 1
        if self.reader_cnt == 0:
            self.writer_lock.release()  # release writer lock when last reader leaves
        self.reader_lock.release()

# Main execution
q = Queue()

n = 20
ts = [threading.Thread(target=q.enque, args=(i, )) for i in range(n)]
ts.extend([threading.Thread(target=q.deque) for i in range(n)])
ts.extend([threading.Thread(target=q.getleft) for i in range(n)])

random.shuffle(ts)

[t.start() for t in ts]
[t.join() for t in ts]

