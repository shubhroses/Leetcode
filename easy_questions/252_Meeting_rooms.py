class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Sort by start time
        Iterate through each element pairwise
        s1, e1, s2, e2
        if s2 < e1: return false
        """
        if not intervals:
            return True
        intervals.sort(key = lambda x:x[0])
        s1 = intervals[0][0]
        e1 = intervals[0][1]

        for s2, e2 in intervals[1:]:
            if s2 < e1:
                return False
            e1 = max(e1, e2)
        return True