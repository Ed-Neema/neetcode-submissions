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
        
        remove = len(array) - n
        if remove == 0:
            head = array[remove].next
        else:
            array[remove-1].next = array[remove].next
        
        return head