# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = 0
        tail = ListNode(0)
        tail.next = head
        while tail.next != None:
            length += 1
            tail = tail.next
        shift = k % length
        idx = ListNode(0)
        idx.next = head
        for i in range(length - shift):
            idx = idx.next
        fakeHead = ListNode(0)
        fakeHead.next = head

        tail.next = head
        fakeHead.next = idx.next
        idx.next = None

        return fakeHead.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    Solution().rotateRight(head, 3)