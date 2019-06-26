# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = []
        self.dfs(root, stack, "")
        return sum(map(lambda item: int(item), stack))
    
    def dfs(self, node, stack, strNum):
        strNum += str(node.val)
        if node.left is None and node.right is None:
            stack.append(strNum)
            return
        if node.left is not None:
            self.dfs(node.left, stack, strNum)
        if node.right is not None:
            self.dfs(node.right, stack, strNum)
        strNum = strNum[:-1]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    Solution().sumNumbers(root)