# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.dfs(root, ret, 0)
        return ret
    
    def dfs(self, node, ret, p):
        if not node:
            return
        if len(ret) <= p:
            ret.append(node.val)
        self.dfs(node.right, ret, p+1)
        self.dfs(node.left, ret, p+1)
        