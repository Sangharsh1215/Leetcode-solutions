# Last updated: 3/25/2025, 2:17:05 AM
class Solution(object):
    def countDays(self, days, meetings):
        meetings.sort()
        prev = 0

        for start, end in meetings:
            start = max(start,prev + 1)
            length = end - start + 1
            days -= max(length,0)
            prev = max(prev, end)

        return days
        
        