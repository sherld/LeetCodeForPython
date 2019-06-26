# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fakeHead = ListNode(0)
        fakeHead.next = head
        pre = fakeHead
        cur = head
        nextNode = None
        while cur:
            nextNode = cur.next
            while pre.next is not None and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            cur = nextNode
        return fakeHead.next