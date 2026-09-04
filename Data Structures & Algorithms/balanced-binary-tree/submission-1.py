# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height_imbalance(self, node: TreeNode) -> int:
        #base case: if node is null, h=0
        if not node:
            return 0
        left_height = self.get_height_imbalance(node.left)
        right_height = self.get_height_imbalance(node.right)
        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height_imbalance(root) != -1
        