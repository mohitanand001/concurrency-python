#https://www.lintcode.com/problem/2462/description
# you can import any package that you need here
# write your code here

import threading
import random

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        """
        @param capacity: maximum queue size
        """
        self.head = -1
        self.tail = -1
        self._size = 0
        self.capacity = capacity
        self.elements = [None] * self.capacity
        self.turn_lock = threading.Condition() 

    def enqueue(self, element: int) -> None:
        """
        @param element: the element given to be added
        @return: nothing
        """

        with self.turn_lock:
            self.turn_lock.wait_for(
                lambda: self._size < self.capacity
            )

            if self.tail == -1:
                self.head = 0
                self.tail = 0
                self._size = 1

                self.elements[self.tail] = element
                self.turn_lock.notify_all()
                return
            self._size +=1
            self.tail = (self.tail + 1) % self.capacity
            self.elements[self.tail] = element
            self.turn_lock.notify_all()
            

    def dequeue(self) -> int:
        """
        @return: pop an element from the front of queue
        """


        with self.turn_lock:
            self.turn_lock.wait_for(
                lambda: self._size > 0
            )

            self._size -=1
            val = self.elements[self.head]
            if self._size == 0:
                self.head = -1
                self.tail = -1

                self.turn_lock.notify_all()
                return val
            self.head = (self.head + 1)%self.capacity
            self.turn_lock.notify_all()
            return val
                



    def size(self) -> int:
        """
        @return: size of queue
        """

        return self._size

