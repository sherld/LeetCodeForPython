# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = dummyHead
        for i in range(m-1):
            p = p.next
        lastNode = p.next
        for i in range(n-m):
            tmp = lastNode.next
            lastNode.next = tmp.next
            tmp.next = p.next
            p.next = tmp
        return dummyHead.next