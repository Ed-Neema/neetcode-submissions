# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node:TreeNode, p:TreeNode, q:TreeNode):
        global lca
        
        if not node:
            return False
        
        node_is_p_or_q = node == p or node == q
        left_contains_p_or_q = self.dfs(node.left, p, q)
        right_contains_p_or_q = self.dfs(node.right, p, q)

        if(node_is_p_or_q + left_contains_p_or_q + right_contains_p_or_q) == 2:
            lca = node
        return node_is_p_or_q or left_contains_p_or_q or right_contains_p_or_q


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs(root, p, q)
        return lca
