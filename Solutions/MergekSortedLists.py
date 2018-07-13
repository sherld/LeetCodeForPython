# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = list(filter(lambda x:x, lists))
        num = len(lists)
        interval = 1
        while interval < num:
            for i in range(0, num - interval, 2*interval):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval = interval * 2
        return lists[0] if num > 0 else lists


    def mergeTwoLists(self, l1, l2):
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

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(0)
    Solution().mergeKLists([l1,l2])