class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        curr = self.head
        ele = []
        while curr:
            ele.append(str(curr.data))
            curr = curr.next
        return '->'.join(ele)


    def pushback(self, val):
        node = Node(val)
        
        if self.head is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def pushfront(self, val):
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
            return
        tmp = self.head
        self.head = node
        self.head.next = tmp

    def popback(self):
        if self.head is None:
            print("empty list, can't pop from back")
            return
        val = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return val
        tmp = self.tail
        self.tail = self.tail.prev
        tmp.prev = None
        self.tail.next = None
        return val

    def popfront(self):
        if self.head is None:
            print("empty list, can't pop from front")
            return
        val = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return val

        tmp = self.head
        self.head = self.head.next
        self.head.prev = None
        tmp.next = None

        return val

from pdb import set_trace as bp
bp()


dll = DLL()
dll.pushback(1)

print(dll)
