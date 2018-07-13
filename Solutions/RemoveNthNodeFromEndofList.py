# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummyHead = ListNode(0)
        dummyHead.next = head
        leftIdx = dummyHead
        rightIdx = dummyHead
        for i in range(n):
            rightIdx = rightIdx.next
        while rightIdx.next != None:
            leftIdx = leftIdx.next
            rightIdx = rightIdx.next
        leftIdx.next = leftIdx.next.next
        return dummyHead.next
        