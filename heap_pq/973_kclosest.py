import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def eucdistance(x,y):
            return math.sqrt(x*x + y*y)

        
        heap = []
        heapq.heapify(heap)

        for x,y in points:
            heapq.heappush(heap, (eucdistance(x,y), (x,y)))

        ans = []
        for i in range(k):
            (dist, (x,y)) = heapq.heappop(heap)
            ans.append([x,y])
            
        return ans
            

        

        
