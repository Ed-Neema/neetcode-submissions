# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Need to keep track of the previous node
        #Need to save a reference to the next node
        #Looping and processing until the current node is null

        previous = None
        current = head
        

        while current is not None:
            next_node = current.next

            #reverse the pointer
            current.next = previous 
            #update previous
            previous = current
            #move the current to the next node
            current = next_node
        #after were done traversing the whole list, the previous (last node becomes the first node)
        
        return previous