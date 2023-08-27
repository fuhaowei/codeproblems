import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        temp = 0
        for i in range(k):
            temp = heapq.heappop(nums)

        return -temp