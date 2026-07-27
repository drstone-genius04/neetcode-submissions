"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:

            return 0

        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        start = 0
        end = 0

        rooms = 0
        max_rooms = 0

        while start < len(intervals):

            # Need a new room
            if starts[start] < ends[end]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start += 1

            # A meeting ended, reuse a room
            else:
                rooms -= 1
                end += 1

        return max_rooms


        

        


      

        