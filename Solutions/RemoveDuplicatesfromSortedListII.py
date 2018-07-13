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
        idx = dummyHead
        flag = False
        while idx.next != None and idx.next.next != None:
            if idx.next.val == idx.next.next.val:
                flag = True
                idx.next = idx.next.next
            else:
                if not flag:
                    idx = idx.next
                else:
                    flag = False
                    idx.next = idx.next.next
        if flag:
            idx.next = idx.next.next
        return dummyHead.next

if __name__ == "__main__":
    dummyHead = ListNode(0)
    p = dummyHead
    array = [1,2,3,3,4,4,5]
    for v in array:
        p.next = ListNode(v)
        p = p.next
    Solution().deleteDuplicates(dummyHead.next)