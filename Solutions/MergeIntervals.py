# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        ret = []
        if not intervals:
            return ret
        intervals.sort(key=lambda x: x.start)
        ret.append(intervals[0])
        for item in intervals[1:]:
            if ret[-1].end >= item.start:
                ret[-1].end = max(ret[-1].end, item.end)
            else:
                ret.append(item)
        return ret

    def mergeMine(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        if not intervals:
            return ret
        sortedIntervals = sorted(intervals, key=lambda x : x.start)
        lo = sortedIntervals[0].start
        hi = sortedIntervals[0].end
        for item in sortedIntervals:
            if hi >= item.start:
                hi = max(hi, item.end)
            else:
                ret.append(Interval(lo, hi))
                lo = item.start
                hi = item.end
        ret.append(Interval(lo, hi))
        return ret

if __name__ == '__main__':
    Solution().merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)])