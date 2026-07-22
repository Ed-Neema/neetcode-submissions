# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if list is empty:
        if head is None:
            return False
        visited = [] #I'm appending a reference of the node
        tail = head

        while tail is not None:
            if tail in visited:
                return True
            else:
                visited.append(tail)
            tail = tail.next
        return False


        