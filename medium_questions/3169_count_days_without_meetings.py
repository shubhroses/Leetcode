class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        1. Merge intervals
        2. For all intervals, iterate and add to visited set
        3. Iterate through days if not in visited increment count
        """
        if not meetings:
            return days
        
        meetings.sort()
        merged = []
        l, r = meetings[0]
        
        for s, e in meetings[1:]:
            if s <= r:
                r = max(r, e)
            else:
                merged.append((l, r))
                l, r = s, e
        merged.append((l, r))
        
        # Calculate the total number of days with meetings
        days_with_meetings = sum(r - l + 1 for l, r in merged)
        
        # Total available days without meetings
        return days - days_with_meetings

        # 3169_count_days_without_meetings.py