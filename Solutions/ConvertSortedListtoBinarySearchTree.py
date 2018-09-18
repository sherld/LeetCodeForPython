# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.dfs(head, None)
    
    def dfs(self, head, tail):
        if head == tail:
            return None
        fast = head
        slow = head
        while fast.next != tail and fast.next.next != tail:
            fast = fast.next.next
            slow = slow.next
        node = TreeNode(slow.val)
        node.left = self.dfs(head, slow)
        node.right = self.dfs(slow.next, tail)
        return node