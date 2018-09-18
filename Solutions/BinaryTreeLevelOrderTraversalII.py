# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ret = []
        nodeList = []
        nodeList.append(root)
        while nodeList:
            tmpList = []
            valList = []
            for node in nodeList:
                if node.left:
                    tmpList.append(node.left)
                if node.right:
                    tmpList.append(node.right)
                valList.append(node.val)
            nodeList = tmpList
            ret.insert(0, valList)
        return ret