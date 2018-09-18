# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodeList = []
        ret = []
        flag = True
        if not root:
            return ret
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
            ret.append(valList if flag else list(reversed(valList)))
            flag = not flag
        return ret

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))
