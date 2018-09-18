# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.preNode = None
        self.dfs(root)
    
    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.right)
        self.dfs(node.left)
        node.right = self.preNode
        node.left = None
        self.preNode = node