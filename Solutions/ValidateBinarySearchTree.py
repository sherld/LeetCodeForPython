# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, -math.inf, math.inf)
    
    def dfs(self, node, minVal, maxVal):
        if node is None:
            return True
        if node.val < minVal or node.val > maxVal:
            return False
        return self.dfs(node.left, minVal, node.val) and self.dfs(node.right, node.val, maxVal)