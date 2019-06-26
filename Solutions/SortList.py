# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fakeHead = ListNode(0)
        fakeHead.next = head
        slow = fakeHead
        fast = fakeHead
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        tmpNode = slow.next
        slow.next = None
        leftHead = self.sortList(fakeHead.next)
        rightHead = self.sortList(tmpNode)
        return self.merge(leftHead, rightHead)
    
    def merge(self, leftHead, rightHead):
        fakeHead = ListNode(0)
        p = fakeHead
        while leftHead or rightHead:
            if not leftHead:
                p.next = rightHead
                break
            elif not rightHead:
                p.next = leftHead
                break
            else:
                if leftHead.val < rightHead.val:
                    p.next = leftHead
                    leftHead = leftHead.next
                else:
                    p.next = rightHead
                    rightHead = rightHead.next
                p = p.next
        return fakeHead.next

if __name__ == "__main__":
    node = ListNode(4)
    node.next = ListNode(2)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)
    Solution().sortList(node)