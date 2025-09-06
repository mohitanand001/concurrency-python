
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
       self.head = None
       self.tail = None
       self.size = 0

    def enque(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
            self.size = 1
            return
        self.tail.next = node
        self.tail = node
        self.size +=1

    def deque(self):
       
       if self.get_size() == 0:
           raise IndexError("cannot deque empty queue")
       
       front = self.head
       if self.head == self.tail:
           self.head = None
           self.tail = None
           self.size = 0
           print("data is ", front.data)
           return front.data

       self.head = self.head.next
       self.size -=1
       print("data is", front.data)
       return front.data

    def peek(self):
       if self.get_size() == 0:
           raise IndexError("cannot peek an empty queue")

       return self.head.data

    def get_size(self):
        return self.size

    def __str__(self):
        """Return a string representation of the queue"""
        if self.get_size() == 0:
             return "Queue is empty"

        current = self.head
        d = []
        while current:
            d.append(str(current.data))
            current = current.next
        return '->'.join(d)


q = Queue()

print(q)

q.enque(1)
print(q)
q.enque(2)
print(q)
q.enque(5)
q.enque(7)
q.enque(10)
q.enque(11)
print(q)
q.deque()
print(q)
q.deque()
print(q)
q.peek()
q.peek()
q.peek()
q.peek()

