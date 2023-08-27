#gist -> do the stuff u need the most first for shortest time.

#maintain deque for cooldown tasks with the next time they can be loaded in
#maintain heap for tasks not on cooldown, since need do the most freq tasks first
#done only when queue + heap is empty

import heapq
from collections import Counter
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        time1 = 0
        counts = Counter(tasks)

        queue = deque()

        heap = []
        heapq.heapify(heap)

        for key, val in counts.items():
            heapq.heappush(heap, -val)

        while (heap) or queue:

            #check if queue hv tasks that r already done loading
            while queue and time1 >= queue[0][1]:
                val,thistime = queue.popleft()
                heapq.heappush(heap, val)

            #queue all cleared, let's process
            if heap:
                val = heapq.heappop(heap)
                #if there's still tasks left, put on freezer queue

                if val < -1:
                    queue.append((val + 1, time1 + n + 1))
            
            time1 += 1

        return time1
            

                 

