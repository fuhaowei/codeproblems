class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if not intervals:
            return True


        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]

        for interval in intervals[1:]:
            xstart, xend = interval[0], interval[1]
            ystart, yend = res[-1][0], res[-1][1]

            overlap = min(yend, xend) - max(xstart, ystart)

            if overlap <= 0:
                res.append(interval)

            else:
                return False


        return True

        

        # 1  3
        #      5 6

        # min end - max start
        # 3-5