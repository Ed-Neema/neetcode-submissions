# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length of the linkedlist -> O(n)
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next

        #Remove element
        remove = length - n
        curr = head
        prev = None
        index = 0

        if remove == 0:
            head = head.next
            return head
            

        while curr:
            if index == remove:
                prev.next = curr.next
                break
            else:
                index+=1
                prev = curr
                curr = curr.next
        return head

