class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # we'll return the next of this node. Just using it to intialize the list
        tail_pointer = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail_pointer.next = list1
                list1 = list1.next
            else: #if list2.val is larger or equal to list1
                tail_pointer.next = list2
                list2 = list2.next
            #update the tailpointer
            tail_pointer = tail_pointer.next
        
        #check if there are remaining nodes
        if list1:
            tail_pointer.next = list1
        elif list2:
            tail_pointer.next = list2
        return dummy.next
