# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        array = []
        curr = head

        while curr:
            array.append(curr)
            curr = curr.next
        
        change = len(array) - n
        if change == 0:
            head = array[change].next
        else:
            array[change-1].next = array[change].next
        
        return head