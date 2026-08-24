# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case -> if root it None
        if not root:
            return None
        #we need to swap out the left and right subtrees
        root.left, root.right = root.right, root.left
        #recursively call invert on left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        