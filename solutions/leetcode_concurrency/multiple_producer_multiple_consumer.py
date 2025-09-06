import threading
import random


class ProducerConsumer:

    def __init__(self, N):
        if N == 0:
            raise ValueError("cannot have a buffer of size 0")

        self.buffer = []
        self.capacity = N
        self.size = 0
        self.head = -1
        self.tail = -1
    


    def produce(self, v):
        
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.buffer[self.tail] = v
            self.size = 1

        if (self.tail + 1) % self.capacity == self.head:
            print("cannt produce, size exceeded")

        self.tail = (self.tail + 1)%self.capacity
        self.buffer[self.tail] = val
        self.size+=1

    def consume(self):

        if self.head == -1:
            print("empty buffer, cant' consume")
            return

        val = self.buffer[self.head]
        self.size -=1
        if self.size == 0:
            self.head = -1
            self.tail = -1
            return val

        self.head = (self.head + 1) % self.capacity
        return val



pc = ProducerConsumer(5)

