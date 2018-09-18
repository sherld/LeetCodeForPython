# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        if root is None:
            return ret
        self.dfs(root, [], ret, sum)
        return ret
    
    def dfs(self, node, stack, ret, val):
        if node.val == val and node.left is None and node.right is None:
            stack.append(node.val)
            ret.append(list(stack))
            stack.pop()
            return
        stack.append(node.val)
        if node.left is not None:
            self.dfs(node.left, stack, ret, val - node.val)
        if node.right is not None:
            self.dfs(node.right, stack, ret, val - node.val)
        stack.pop()