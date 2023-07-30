#key takeaway -> backtracking all the possible paths
#we stop immediately when it's not a palindrome
#only add at the end
#to generate all possible substrings
#just look through with nested for
class Solution:
    def partition(self, s: str) -> list[list[str]]:

        #check if substring is a palindrome
        def isPalin(s):
            return s == s[::-1]
        
        def backtrack(start, path):
            if start >= len(s):
                res.append(path)
                return

            #hv to check the possible substrings now
            for idx in range(start + 1, len(s) + 1):
                if isPalin(s[start:idx]):
                    backtrack(idx, path + [s[start:idx]])

        res = []
        backtrack(0, [])
        return res