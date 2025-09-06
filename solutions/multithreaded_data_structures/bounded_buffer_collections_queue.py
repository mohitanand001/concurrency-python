# you can import any package that you need here
# write your code here
#https://www.lintcode.com/problem/2462/description
import threading

from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        """
        @param capacity: maximum queue size
        """
        self.elements = deque()
        self.capacity = capacity
        self.turn_lock = threading.Condition()

    def enqueue(self, element: int) -> None:
        """
        @param element: the element given to be added
        @return: nothing
        """
        with self.turn_lock:
            self.turn_lock.wait_for(
                lambda: len(self.elements) < self.capacity
            )
            self.elements.append(element)
            self.turn_lock.notify_all()
        

    def dequeue(self) -> int:
        """
        @return: pop an element from the front of queue
        """
        with self.turn_lock:
            self.turn_lock.wait_for(
                lambda: len(self.elements) > 0
            )
            val = self.elements.popleft()
            self.turn_lock.notify_all()
            return val


    def size(self) -> int:
        """
        @return: size of queue
        """

        return len(self.elements)
