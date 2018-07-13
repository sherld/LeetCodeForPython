# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        index1 = l1
        index2 = l2
        fake_head = ListNode(0)
        index3 = fake_head
        count = 0
        while True:
            if index1 == None and index2 == None:
                if count == 1:
                    index3.next = ListNode(1)
                    break
                else:
                    break
            elif index1 == None:
                sum = count + index2.val
                index3.next = ListNode(sum % 10)
                count = sum // 10
                index2 = index2.next
                index3 = index3.next
            elif index2 == None:
                sum = count + index1.val
                index3.next = ListNode(sum % 10)
                count = sum // 10 
                index1 = index1.next
                index3 = index3.next
            else:
                sum = count + index1.val + index2.val
                index3.next = ListNode(sum % 10)
                count = sum // 10
                index1 = index1.next
                index2 = index2.next
                index3 = index3.next
        return fake_head.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    ret = Solution().addTwoNumbers(l1, l2)
    while ret != None:
        print(ret.val)
        ret = ret.next