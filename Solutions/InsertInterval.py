# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ret = []
        ret.append(newInterval)
        for item in intervals:
            if item.end < ret[-1].start:
                ret.insert(-1, item)
            elif item.start > ret[-1].end:
                ret.append(item)
            else:
                ret[-1].start = min(ret[-1].start, item.start)
                ret[-1].end = max(ret[-1].end, item.end)
        return ret

if __name__ == '__main__':
    Solution().insert([Interval(1,2),Interval(3,5),Interval(8,10),Interval(12,16)], Interval(4,8))