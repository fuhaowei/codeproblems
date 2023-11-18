class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a == b

# 问有没有edge case，有没有其他方法节约空间

#save space -> sort then return, slower on time o(nlogn) for fastest sort (binary)
#o(n) -> give every unique char a prime, multiply everything together then compare bcs you get unique number (but obv slow when long)
#are there edge cases to using a dictionary for this? i guess if we consider A and a to be the same letter
#then we would have an issue
