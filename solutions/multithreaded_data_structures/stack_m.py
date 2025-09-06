import threading
import random
import time

class Stack:

    def __init__(self):
        self.readers = 0
        self.writer_lock = threading.Lock()
        self.reader_lock = threading.Lock()
        self.elements = []

    def pop(self):
        self.writer_lock.acquire()
        if len(self.elements) > 0:
            val = self.elements[-1]
            print("value of element to be popped is", val)
            self.elements.pop() 
        else:
            val = -100
        self.writer_lock.release()
        return val


    def push(self, val):
        self.writer_lock.acquire()
        self.elements.append(val)
        self.writer_lock.release()

    def peek(self):
        self.reader_lock.acquire()
        self.readers +=1

        if self.readers == 1:
            self.writer_lock.acquire()

        self.reader_lock.release()

        if len(self.elements) > 0:
           print(f"reading top {self.elements[-1]}, readers count ={self.readers}")
        else:
            print(f"empty list,readers count ={self.readers}")


        self.reader_lock.acquire()
        self.readers -=1

        if self.readers == 0:
            self.writer_lock.release()

        print(f"reading done readers count ={self.readers}")
        self.reader_lock.release()





s = Stack()
N = 20
ts = [threading.Thread(target=s.pop) for i in range(N)]
ts.extend([
    threading.Thread(target=s.push, args=(i, )) for i in range(N)])
ts.extend([
    threading.Thread(target=s.peek,) for i in range(N)])


random.shuffle(ts)

[t.start() for t in ts]
[t.join() for t in ts]
