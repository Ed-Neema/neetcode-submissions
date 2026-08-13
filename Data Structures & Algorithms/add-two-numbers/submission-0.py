# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        var1 = ""
        var2 = ""

        pointer1 = l1
        pointer2 = l2

        while pointer1:
            var1 += str(pointer1.val)
            pointer1 = pointer1.next
        while pointer2:
            var2 += str(pointer2.val)
            pointer2 = pointer2.next
        
        rev_var1 = var1[::-1]
        rev_var2 = var2[::-1]

        result = str(int(rev_var1) + int(rev_var2))

        head = ListNode()
        prev = None
        reversed_result = result[::-1]
        

        for n in str(reversed_result):
            new_node = ListNode(n)
            if prev == None:
                head.next = new_node
            else:
                prev.next = new_node
            prev = new_node
        
        return head.next




        
        