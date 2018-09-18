# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        stack = []
        ret = []
        if root == None:
            return ret
        stack.append(root)
        while stack:
            nodeList = []
            valList = []
            for item in stack:
                if item.left != None:
                    nodeList.append(item.left)
                if item.right != None:
                    nodeList.append(item.right)
                valList.append(item.val)
            ret.append(valList)
            stack = nodeList
        return ret

