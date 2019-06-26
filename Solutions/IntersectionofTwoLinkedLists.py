# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        a = headA
        b = headB

        # if a & b have different len, then we will stop the loop after second iteration
        while a != b:
            # for the end of first iteration, we just reset the pointer to the head of another linkedlist
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a