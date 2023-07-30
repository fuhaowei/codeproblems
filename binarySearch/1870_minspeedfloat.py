class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
          #there are some base cases i need to figure out

        if hour < len(dist) - 1 or (hour == int(hour) and hour < len(dist) - 1 + 1e-9):
            return -1

        #a function that calculates for each speed, how many hours it takes

        def calculateSpeed(speed):
            totaltime = 0
            for idx in range(len(dist)):
                if idx != len(dist) -1:
                    # print(dist)
                    # print(type(speed))
                    # print(speed)
                    totaltime += math.ceil(dist[idx]/speed - 1e-9)

            totaltime += dist[-1]/ speed

            return totaltime
            

        # binary search

        left, right = 1, max(dist) * (10 ** 6)

        while left < right:
            mid = (left + right) // 2
            if calculateSpeed(mid) > hour:
                left = mid + 1

            else:
                right = mid

        return left