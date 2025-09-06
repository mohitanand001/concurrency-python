'''
https://leetcode.com/discuss/interview-question/6282505/Rubrik-or-Systems-Coding-or-Senior-Software-Engineer
Implement a FIFO Queue:

put(int): Adds item into queue
get() int: Removes and returns item in queue in FIFO order
Requirements:

Fix sized memory buffer []int
No dynamic memory allocation (not allocating new memory or objects as part of put + get()).
Follow up:

Support for multiple thread access.
Two queues which share this same fix sized memory buffer
Need to support FIFO ordering for each queue individually.
The size of this int[] (100MB - > 1GB+)
We want to make sure usage of this fix sized array can be dynamically adjusted based on each indiv. queue's usage.
Minimize memory wastage
'''




class CircularQueue:

    def __init__(self, N):
        self.head = -1
        self.tail = -1
        self.maxcapacity = N
        self.size = 0
        self.elements = [None]*self.maxcapacity
    
    def empty(self):
        return self.size == 0


    def print_all(self):
        indx = self.head
        ans=''
        while True:
            print("indx is",indx)
            if indx == self.tail:
                ans +=','+str(self.elements[indx])
                break
            ans+=','+str(self.elements[indx])
            indx = (indx + 1)%self.maxcapacity
        print(ans)


    def enque(self, val):
        if self.size == self.maxcapacity:
            print("buffer  size full")
            return
        if self.empty():
            self.head = 0
            self.tail = 0
            self.size = 1
            self.elements[self.tail] = val
            self.print_all()
            return

        if (self.tail + 1) % self.maxcapacity == self.head:
            print("buffer is full, can't enque")
            return

        self.tail = (self.tail + 1)%self.maxcapacity
        self.elements[self.tail] = val
        self.print_all()
        self.size+=1

    def deque(self):
        if self.empty():
            print("cant deque an empty queue")
            return
        val = self.elements[self.head]
        self.head = (self.head + 1)%self.maxcapacity
        self.size -=1
        if self.empty():
            self.head = -1
            self.tail = -1

        self.print_all()

        return val

    def peek(self):

        if self.empty():
            print("can't peak empty queue")
            return
        return self.elements[self.head]


cq = CircularQueue(5)

from pdb import set_trace as bp
bp()



