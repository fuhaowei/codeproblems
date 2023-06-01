class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #monotonic because if nkg ship can, n+1 kg ship will also be able to ship
        #max will the sum of all the weights possible
        min = 1
        max = sum(weights)


        def shipthis(cap, weights):
            currentw = 0
            idx = 0
            days = 1
            while (idx < len(weights)):
                if (currentw + weights[idx] <= cap):
                    currentw += weights[idx]
                    idx += 1
                elif weights[idx] > cap:
                    days = -1
                    break
                else:
                    currentw = 0
                    days += 1
            return days

        
        while (min < max):
            
            #since we r looking for min, we should floor divide so min

            mid = (min + max )// 2

            if shipthis(mid, weights) == -1:
                min = mid + 1

            elif shipthis(mid, weights) <= days:
                max = mid

            else:
                min = mid + 1

        return min
