# Leetcode 252: Meeting Rooms
# Link: https://leetcode.com/problems/meeting-rooms/

from typing import List

class Solution:
    '''
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    '''
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
                
        return True