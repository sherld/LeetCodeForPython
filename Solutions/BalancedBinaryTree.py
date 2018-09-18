# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1

    def dfs(self, node):
        if node is None:
            return 0
        valLeft =  self.dfs(node.left)
        if valLeft == -1:
            return -1
        valRight = self.dfs(node.right)
        if valRight == -1:
            return -1
        if abs(valLeft - valRight) > 1:
            return -1
        return max(valLeft, valRight) + 1