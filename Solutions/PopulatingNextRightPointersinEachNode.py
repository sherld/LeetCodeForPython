# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        nodeList = []
        nodeList.append(root)
        while nodeList:
            tmpList = []
            for node in nodeList:
                if node.left is not None:
                    tmpList.append(node.left)
                if node.right is not None:
                    tmpList.append(node.right)
            for i in range(len(tmpList)-1):
                tmpList[i].next = tmpList[i+1]
            nodeList = tmpList


        