# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type fast: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        cnt = 0
        while p2 != None:
            if cnt == k:
                p1 = self.reserve(p1, p2)
                p2 = p1.next
                cnt = 0
            else:
                p2 = p2.next
            cnt += 1
        return dummy.next

    def reserve(self, head, tail):
        idx = head.next
        while head.next != tail:
            tmp = head.next
            head.next = idx.next
            idx.next= idx.next.next
            head.next.next = tmp
        return idx
        

if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    Solution().reverseKGroup(l, 2)       