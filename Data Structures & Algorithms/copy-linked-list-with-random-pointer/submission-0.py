"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        old_pointer = head
        new_pointer = dummy
        hashmap = {}
        
        while old_pointer:
            new = Node(old_pointer.val)
            hashmap[old_pointer] = new
            new_pointer.next = new
            new_pointer = new_pointer.next
            old_pointer = old_pointer.next

        new_pointer = dummy.next
        old_pointer = head

        while new_pointer:
            #incase it's None
            if old_pointer.random:
                new_pointer.random = hashmap[old_pointer.random]
            else:
                new_pointer.random = None
            # new_pointer.random = hashmap.get(old_pointer.random)
            new_pointer = new_pointer.next
            old_pointer = old_pointer.next
        
        return dummy.next