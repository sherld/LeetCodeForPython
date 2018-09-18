# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)
    
    def dfs(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        
        nodeList = []

        for i in range(start, end+1):
            leftList = self.dfs(start, i - 1)
            rightList = self.dfs(i+1, end)

            for leftNode in leftList:
                for rightNode in rightList:
                    root = TreeNode(i)
                    root.left = leftNode
                    root.right = rightNode
                    nodeList.append(root)
        return nodeList

if __name__ == '__main__':
    Solution().generateTrees(3)
        