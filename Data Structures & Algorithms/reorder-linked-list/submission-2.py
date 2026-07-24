# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Need to find the middle point of the list - using fast and slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None #its the end of the first list

        #need to reverse second half
        previous = None
        while second:
            tmp = second.next
            second.next = previous
            previous = second
            second = tmp

        #now we merge the two halfs of the list
        #beginning of second list is the previous pointer
        first = head
        second = previous #new head of second list

        while second:
            #store the next nodes in temporary variables
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            #shift the pointers
            first, second = tmp1, tmp2

        