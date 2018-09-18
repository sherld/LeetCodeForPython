# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.dfs(root, sum)
    
    def dfs(self, node, val):
        if val == node.val and node.left is None and node.right is None:
            return True
        if node.left is not None:
            if self.dfs(node.left, val - node.val):
                return True
        if node.right is not None:
            if self.dfs(node.right, val - node.val):
                return True
        return False

if __name__ == '__main__':
    node = TreeNode(5)
    node.left = TreeNode(4)
    node.left.left = TreeNode(11)
    node.left.left.right = TreeNode(2)
    print(Solution().hasPathSum(node, 22))