from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            temp = list(string)
            temp.sort()
            tempstr = str(temp)
            anagrams[tempstr].append(string)

        ans = []
        for vals in anagrams.values():
            ans.append(vals)

        return ans

         

        