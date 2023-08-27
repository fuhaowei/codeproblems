import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newstones = [-x for x in stones]
        heapq.heapify(newstones)

        while len(newstones) > 1:
            stone1 = heapq.heappop(newstones)
            stone2 = heapq.heappop(newstones)
            if stone1 == stone2:
                continue
            else:
                temp = abs(stone1) - abs(stone2) 
                heapq.heappush(newstones, -temp)


        if len(newstones) == 1:
            return -newstones[0]
        else:
            return 0

        
