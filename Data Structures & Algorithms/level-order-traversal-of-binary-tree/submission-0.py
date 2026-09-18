# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        level = 1
        queue.append([root,level])
        res = []

        while queue:
            node, nl = queue.pop(0)

            if not node:
                continue

            if len(res) > 0:
                if nl == level:
                    res[-1].append(node.val)
                else:
                    new_list = []
                    new_list.append(node.val)
                    res.append(new_list)
            else:
                new_list = []
                new_list.append(node.val)
                res.append(new_list)
            
            if node.left:
                queue.append([node.left, nl+1])
            if node.right:
                queue.append([node.right, nl+1])
            
            level = nl

        return res


        