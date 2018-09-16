# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            
            else:
                root = stack.pop()
                root = root.right
        return res
