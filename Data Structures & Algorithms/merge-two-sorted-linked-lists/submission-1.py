class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        new_head = ListNode()
        #check for empty lists
        if p1 is None and p2 is not None:
            return p2
        elif p2 is None and p1 is not None:
            return p1
        elif p1 is None and p2 is None:
            return p1

        #determine which head is smaller to start the new list
        if p1.val <= p2.val:
            new_head.val = p1.val
            new_head.next = p1.next
            p1 = p1.next
        else: 
            new_head.val = p2.val
            new_head.next = p2.next
            p2 = p2.next
        curr = new_head

        while p1 is not None:
            if (p2 is None) or (p2 is not None and p1.val <= p2.val):
                new_node = ListNode(p1.val, p1.next)
                curr.next = new_node
                curr = new_node
                p1 = p1.next
            elif p2 is not None and p1.val > p2.val:
                new_node = ListNode(p2.val, p2.next)
                curr.next = new_node
                curr = new_node
                p2 = p2.next
        while p2 is not None:
            new_node = ListNode(p2.val, p2.next)
            curr.next = new_node
            curr = new_node
            p2 = p2.next

        return new_head