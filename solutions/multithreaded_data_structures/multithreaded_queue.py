from collections import deque
import threading
import time
import random


class Queue:

    def __init__(self):
        self._elements = deque()
        self.reader_lock = threading.Lock()
        self.reader_cnt = 0
       
        self.writer_lock = threading.Lock()


    def enque(self, val):
        self.writer_lock.acquire()

        self._elements.append(val)

        self.writer_lock.release()

    def deque(self):
        '''
        involves modifying the data structure,
        so don't let multiple threads enter.
        '''
        self.writer_lock.acquire()
        if len(self._elements) > 0:
            val = self._elements.popleft()
        else:
            val = -10


        self.writer_lock.release()

        return val 

    def getright(self):
        pass
        '''
        now what if we need to access this function in a thread safe fashion as well.

        '''
    def getleft(self):
        '''
        let N readers get into critical  section,
        but only when it's not acquired by any writer
        i.e. the  lock is not acquired by 
        enque and deque functions.
        '''

        self.reader_lock.acquire()
        self.reader_cnt+=1
        if self.reader_cnt == 1:
            print("acquiring writer lock")
            self.writer_lock.acquire()

        #self.reader_lock.notify_all()
        self.reader_lock.release()

        # many readers can enter this section 
        # and do the "non-critical" section 
        # activity,
        # since the following 2 lines are not 
        # under any influence of lock, they can be reached by multiple threads
        if len(self._elements) > 0:
          print(f"the left element is {self._elements[0]} and the reader count is {self.reader_cnt}")
        else:
            print(f"empty queue and the reader count is {self.reader_cnt}")
        time.sleep(2)

        self.reader_lock.acquire()
        self.reader_cnt-=1
        print("done reading, readers count", self.reader_cnt)
        
        if self.reader_cnt == 0:
            #print("lock status", self.writer_lock.acquire())
            #self.writer_lock.notify_all()
            self.writer_lock.release()

        #self.reader_lock.notify_all()
        self.reader_lock.release()




q = Queue()

n = 20
ts = [threading.Thread(target=q.enque, args=(i, )) for i in range(n)]
ts.extend([threading.Thread(target=q.deque) for i in range(n)])
ts.extend([threading.Thread(target=q.getleft) for i in range(n)])
ts.insert(0, threading.Thread(target=q.enque, args=(10, ) ) )
ts.insert(0, threading.Thread(target=q.enque, args=(11, ) ) )
ts.insert(0, threading.Thread(target=q.enque, args=(12, ) ) )
ts.insert(0, threading.Thread(target=q.enque, args=(13, ) ) )


random.shuffle(ts)
[t.start() for t in ts]
[t.join() for t in ts]
