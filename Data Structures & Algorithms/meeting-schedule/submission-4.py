"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i, m1 in enumerate(intervals):
            for m2 in intervals[i+1:]:
                if min(m1.end, m2.end) > max(m1.start, m2.start):
                    return False
        return True