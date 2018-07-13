# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = dummyHead
        while p.next != None and p.next.next != None:
            if p.next.next.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return dummyHead.next