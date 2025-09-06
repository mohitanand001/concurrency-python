#https://www.lintcode.com/problem/2462/description
import threading

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        """
        @param capacity: maximum queue size
        """
        self.head = -1
        self.tail = -1
        self._size = 0  # Renamed to avoid conflict with method name
        self.capacity = capacity
        self.elements = [None] * self.capacity
        self.turn_lock = threading.Condition()

    def enqueue(self, element: int) -> None:
        """
        @param element: the element given to be added
        @return: nothing
        """
        with self.turn_lock:
            self.turn_lock.wait_for(lambda: self._size < self.capacity)

            if self.tail == -1:  # Initialize head & tail only once
                self.head = self.tail = 0

            self.elements[self.tail] = element
            self.tail = (self.tail + 1) % self.capacity  # Circular increment
            self._size += 1  # Increase count

            self.turn_lock.notify_all()

    def dequeue(self) -> int:
        """
        @return: pop an element from the front of queue
        """
        with self.turn_lock:
            self.turn_lock.wait_for(lambda: self._size > 0)

            val = self.elements[self.head]
            self._size -= 1  # Decrease count before modifying pointers

            if self._size == 0:
                self.head = self.tail = -1  # Reset pointers when empty
            else:
                self.head = (self.head + 1) % self.capacity  # Circular increment

            self.turn_lock.notify_all()
            return val

    def size(self) -> int:
        """
        @return: size of queue
        """
        return self._size  # Use _size to avoid name conflict

