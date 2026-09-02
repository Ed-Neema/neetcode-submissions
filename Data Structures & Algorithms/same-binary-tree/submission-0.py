# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = [p]
        stack_q = [q]
        result = True

        while stack_p:
            if not stack_q:
                return False

            popped_p = stack_p.pop()
            popped_q = stack_q.pop()

            # Both are None
            if popped_p is None and popped_q is None:
                continue

            # One is None, or their values differ
            if popped_p is None or popped_q is None:
                return False

            if popped_p.val != popped_q.val:
                return False
                
            #add their left and right to respective stacks
           
            stack_p.append(popped_p.left)
            stack_p.append(popped_p.right)
            
            stack_q.append(popped_q.left)
            stack_q.append(popped_q.right)        
        
        return True

            
        