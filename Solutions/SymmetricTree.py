# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, root)
    
    def dfs(self, node1, node2):
        if node1 == None or node2 == None:
            return node1 == node2
        return node1.val == node2.val and self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)