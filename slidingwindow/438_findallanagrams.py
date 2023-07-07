#super tricky -> think about stop condition
#why can't it be all val = 0? 
#sometimes when u have 1 -1, it says it's not valid and not
#anagram within that window, but there is. as long as the
#count is cleared, means there's somethign!

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        left = 0
        right = 0
        lens = len(s)
        count = len(p)
        ans = []

        freqtable = {}
        for letter in p:
            if letter in freqtable:
                freqtable[letter] += 1
            else:
                freqtable[letter] = 1


        while right < lens:

            endchar = s[right]
            if endchar in freqtable:
                freqtable[endchar] -= 1
                if freqtable[endchar] >= 0:
                    count -= 1

                #stopcond noted
                while count == 0:
                    if right - left + 1 == len(p):
                        ans.append(left)
                        
                    startchar = s[left]
                    if startchar in freqtable:
                        freqtable[startchar] += 1
                        if freqtable[startchar] > 0:
                            count += 1
                    left += 1

            right += 1

        return ans
                    
