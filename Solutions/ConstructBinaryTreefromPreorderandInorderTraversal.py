# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(preorder, 0, inorder, 0, len(inorder)-1)
    
    def dfs(self, preorder, preStart, inorder, inStart, inEnd):
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None
        node = TreeNode(preorder[preStart])
        p = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == preorder[preStart]:
                p = i
                break
        node.left = self.dfs(preorder, preStart+1, inorder, inStart, p-1)
        node.right = self.dfs(preorder, preStart+1+p-inStart, inorder, p+1, inEnd)
        return node

        