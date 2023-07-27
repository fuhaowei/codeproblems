class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        res = []
        candidates.sort()

        def dfs(i):
            if sum(res) == target:
                ans.append(res[:])
                return

            if i >= len(candidates) or sum(res) > target:
                return

            res.append(candidates[i])
            dfs(i + 1)

            res.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1

            dfs(i + 1)

        dfs(0)
        return ans