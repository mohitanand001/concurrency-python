#https://leetcode.com/problems/lru-cache/
# accepted solution

class Node:

    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None
        self.prev = None



class LRUCache:


    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
    
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.key2node = dict()


    def get(self, key: int) -> int:
        
        if key  not in self.key2node.keys():
            return -1

        node = self.key2node[key]
        self._remove(node)
        self._add(node)
        return node.v


    def put(self, key: int, value: int) -> None:

        if key in self.key2node.keys():
            node = self.key2node[key]
            self._remove(node)
            node.v = value
            self._add(node)
            return

        if len(self.key2node) == self.capacity:
            n = self.head.next
            self._remove(n)
            self.key2node.pop(n.k)

        
        node = Node(key, value)
        self._add(node)
        self.key2node[key] = node

    def _add(self, node):

        last = self.tail.prev
        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p

        del node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

