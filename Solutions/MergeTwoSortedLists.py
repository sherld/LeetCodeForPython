# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        dummyL1 = ListNode(0)
        dummyL1.next = l1
        dummyL2 = ListNode(0)
        dummyL2.next = l2
        dummyRet = ListNode(0)
        idx = dummyRet
        while dummyL1.next != None or dummyL2.next != None:
            if dummyL1.next == None:
                idx.next = ListNode(dummyL2.next.val)
                dummyL2 = dummyL2.next
                idx = idx.next
            elif dummyL2.next == None:
                idx.next = ListNode(dummyL1.next.val)
                dummyL1 = dummyL1.next
                idx = idx.next
            else:
                val1 = dummyL1.next.val
                val2 = dummyL2.next.val
                if val1 <= val2:
                    idx.next = ListNode(val1)
                    dummyL1 = dummyL1.next
                    idx = idx.next
                else:
                    idx.next = ListNode(val2)
                    dummyL2 = dummyL2.next
                    idx = idx.next
        return dummyRet.next

    # iteratively
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        
    # recursively    
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
    # in-place, iteratively        
    def mergeTwoLists3(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

if __name__ == '__main__':
    # l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(4)
    # l2 = ListNode(1)
    # l2.next = ListNode(3)
    # l2.next.next = ListNode(4)
    l1 = ListNode(1)
    l2 = None
    Solution().mergeTwoLists(l1,l2)