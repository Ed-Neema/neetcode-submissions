# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current is not None:
            # Save the next node before changing any pointers
            next_node = current.next

            # Reverse the pointer
            current.next = previous

            # Move both pointers forward
            previous = current
            current = next_node

        # previous is now the new head
        return previous
        