#sweeping line strategy

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        highest = 0


        room_scans = defaultdict(int)

        #o(n) -> sort is o(logn)

        for start, end in intervals:
            room_scans[start] += 1
            room_scans[end] -= 1

        temp = []
        for (start,count) in room_scans.items():
            temp.append((start,count))
        temp.sort()

        cur = 0
        for (start,count) in temp:
            cur += count
            highest = max(cur, highest)

        return highest

        
        