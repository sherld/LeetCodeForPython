import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxVal = -math.inf
        self.dfs(root)
        return self.maxVal
    
    def dfs(self, node):
        if node is None:
            return 0
        leftVal = max(0, self.dfs(node.left))
        rightVal = max(0, self.dfs(node.right))
        self.maxVal = max(self.maxVal, leftVal + rightVal + node.val)
        return max(leftVal, rightVal) + node.val

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    Solution().maxPathSum(root)