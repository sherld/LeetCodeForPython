# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.dfs(ret, root)
        return ret
    
    def dfs(self, ret, node):
        if node == None:
            return
        self.dfs(ret, node.left)
        ret.append(node.val)
        self.dfs(ret, node.right)