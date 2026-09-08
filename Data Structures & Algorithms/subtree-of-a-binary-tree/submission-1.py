# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if subroot is empty, it will be a subtree of root regardless of whether root is empty or not
        if not subRoot:
            return True
        #in the opposite case: root is empty and subRoot none empty
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, s, t):
        #if both trees are null, subtree condition true
        if not s and not t:
            return True
        
        #one could still be empty, so check if we have both nodes first
        if s and t and s.val == t.val:
            #we stil have to compare the left and right subtrees

            #check if left subtrees match
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right) #check if right subtrees match

            #atleast one of the trees are empty and another none empty
            return False

        