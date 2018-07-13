# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        gtHead = None
        p1 = dummyHead
        p2 = ListNode(0)
        while p1.next != None:
            if p1.next.val < x:
                p1 = p1.next
            else:
                if not gtHead:
                    gtHead = p1.next
                p2.next = p1.next
                p2 = p2.next
                p1.next = p1.next.next
        p2.next = None
        p1.next = gtHead
        return dummyHead.next

if __name__ == "__main__":
    dummyHead = ListNode(0)
    p = dummyHead
    array = [1,4,3,2,5,2]
    for v in array:
        p.next = ListNode(v)
        p = p.next
    Solution().partition(dummyHead.next, 3)
        