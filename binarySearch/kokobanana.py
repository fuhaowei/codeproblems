class Solution(object):

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def nomnom(piles, speed):
            final = 0
            for pile in piles:
                final += (pile + speed - 1)//speed
            return final

        max = 0
        for pile in piles:
            if pile > max:
                max = pile

        #minimum possible: eat 1 at one time
        min = 1
        mid = 0

        while min < max:
            mid = (min + max) // 2
            if nomnom(piles, mid) <= h:
                max = mid
            else:
                min = mid + 1

        return min