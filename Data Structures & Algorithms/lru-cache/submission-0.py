class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
   

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0) #LRU
        self.right = Node(0,0) #MRU
        #initially we need these nodes to be connected to each other
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node): # at right
        prev, next = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            #update this value to most recent used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        #else if key not in cache return -1 as instructed
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        #add to hashmap
        self.cache[key] = Node(key,value)
        #insert into doubly linkedlist
        self.insert(self.cache[key])
        #check capacity constraint
        if len(self.cache) > self.cap:
            #remove from DoublyLinkedList and del from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        
