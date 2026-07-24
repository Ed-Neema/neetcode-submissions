# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Go through the linkedList and store the values in an array
        curr = head
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next

        #Two pointers on left and right
        l,r = 0, len(nodes) - 1
        current = head

        #while r > l, Add left to the list, then add right to the list,
        # Increase left and decrease right
        while r > l:
            #add left
            if current != head:
                new_node = ListNode(nodes[l])
                current.next = new_node
                current = new_node
            #add right
            new_noder = ListNode(nodes[r])
            current.next = new_noder
            current = current.next
            #increment l, decrement r
            l+=1
            r-=1
            if r==l:
                new_node = ListNode(nodes[l])
                current.next = new_node



        

        