# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        nodeList = []
        nodeList.append(root)
        minVal = 1
        while nodeList:
            tmpList = []
            for node in nodeList:
                if node.left is None and node.right is None:
                    return minVal
                if node.left is not None:
                    tmpList.append(node.left)
                if node.right is not None:
                    tmpList.append(node.right)
            minVal += 1
            nodeList = tmpList
        return minVal
        