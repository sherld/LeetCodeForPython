import collections
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        self.recursiveVisitMap = {}

    def getClonedNode(self, node, visitedMap):
        if node:
            if node in visitedMap:
                return visitedMap[node]
            else:
                visitedMap[node] = RandomListNode(node.label)
                return visitedMap[node]
        return None

    def copyRandomListIterative(self, head):
        if head is None:
            return None
        oldNode = head
        newNode = RandomListNode(oldNode.label)
        visitedMap = {}
        visitedMap[oldNode] = newNode

        while oldNode is not None:
            newNode.random = self.getClonedNode(oldNode.random, visitedMap)
            newNode.next = self.getClonedNode(oldNode.next, visitedMap)
            oldNode = oldNode.next
            newNode = newNode.next
        return visitedMap[head]

    def copyRandomListRecursive(self, head):
        if head is None:
            return None
        if head in self.recursiveVisitMap:
            return self.recursiveVisitMap[head]
        
        copyNode = RandomListNode(head.label)
        self.recursiveVisitMap[head] = copyNode

        copyNode.next = self.copyRandomListRecursive(head.next)
        copyNode.random = self.copyRandomListRecursive(head.random)

        return copyNode

    def copyRandomListConcise(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        n = head
        while n:
            dic[n].label = n.label
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]