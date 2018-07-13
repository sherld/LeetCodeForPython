# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        dummy = ListNode(0)
        cur = dummy
        dummy.next = head
        while cur.next != None and cur.next.next != None:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = cur.next.next
            cur.next.next = tmp
            cur = cur.next.next
        return dummy.next

if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    Solution().swapPairs(l)