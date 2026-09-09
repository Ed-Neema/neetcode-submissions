# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #start validation at the root node, which can contain any value. 
        # so we set the initial lower and upper bounds to -infinity and + infinity
        return self.is_within_bounds(root, float('-inf'), float('+inf'))
    def is_within_bounds(self, node:TreeNode, lower_bound:int, upper_bound:int) -> bool:
        #base case: if node is Null, satisfies the BST condition
        if not node:
            return True
        #if current node's value is not within bounds, then not BST
        if not lower_bound < node.val < upper_bound:
            return False
        
        #Else if it is within, then call function recursively to left subtree and right subtree
        #OPTIMIZATION: we can check if left returns true first before we call right
        
        if not self.is_within_bounds(node.left, lower_bound ,node.val):
            return False
        #else if left is BST, call right
        return self.is_within_bounds(node.right, node.val, upper_bound)
        