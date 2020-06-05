"""
Invert a binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        queue = []
        queue.insert(0, root)
        while len(queue) > 0:
            dq = queue.pop()
            tmp = dq.left
            dq.left = dq.right
            dq.right = tmp
            
            if dq.left:
                queue.insert(0, dq.left)
            if dq.right:
                queue.insert(0, dq.right)
        return root
