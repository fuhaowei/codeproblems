class Solution:

    def __init__(self, w: List[int]):
        self.prefixes = []
        cur = 0
        for number in w:
            cur += number
            self.prefixes.append(cur)
        self.totalsum = cur

    def pickIndex(self) -> int:
        offset = random.random() * self.totalsum

        low = 0
        high = len(self.prefixes)

        while low < high:
            curr = (low + high) // 2

            print(curr)

            if self.prefixes[curr] < offset:
                low = curr + 1
            else:
                high = curr

        return low

        #binary search for which idx offset is
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

#prefix sum -> binary search    