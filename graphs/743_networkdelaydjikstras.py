import heapq

#The algorithm is "greedy" in that it always selects the unvisited vertex with the smallest 
# tentative distance to visit next, even if this choice might not appear to lead directly toward 
# the destination. This local optimum choice leads to a globally optimum solution.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjlist = {i:[] for i in range(n+1)}

        for u,v,w in times:
            adjlist[u].append((w, v))

        pq = []
        heapq.heapify(pq)

        for (time, target) in adjlist[k]:
            heapq.heappush(pq,(time,target))

        visited = set()
        visited.add(k)
        time = 0
        for (w,v) in adjlist[k]:
            heapq.heappush(pq, (w,v))
        
        while pq:
            (time1, target1) = heapq.heappop(pq)
            if target1 in visited:
                continue
            else:
                visited.add(target1)
                if len(visited) == n:
                    return time1
                for (w,v) in adjlist[target1]:
                    if v not in visited:
                        heapq.heappush(pq, (w + time1,v))

   
        return -1
