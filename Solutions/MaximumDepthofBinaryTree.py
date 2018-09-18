# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodeList = []
        nodeList.append(root)
        depth = 0
        while nodeList:
            tmpList = []
            for node in nodeList:
                if node.left:
                    tmpList.append(node.left)
                if node.right:
                    tmpList.append(node.right)
            nodeList = tmpList
            depth += 1
        return depth
