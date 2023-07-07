#kinda diff from others. in this case,
#expand window until it fails, then 
#shrink until it passes. then check the top length.
# so kind of the opposite if u feel me. the other one is expand until it passes, then shrink until it fails.
# so it differs based on type of questions ok! 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lens = len(s)
        left = 0
        right = 0
        freqtable = {}

        maxlength = 0

        def cond(freqtable): 

            #failed the condition. shrink!
            return any(val > 1 for val in freqtable.values())

        while right < lens:

            endchar = s[right]
            if endchar in freqtable:
                freqtable[endchar] += 1
            else:
                freqtable[endchar] = 1

            #while i'm failing, keep shrinking
            while cond(freqtable):
                #shrink window
                startchar = s[left]
                freqtable[startchar] -= 1
                if freqtable[startchar] == 0:
                    del freqtable[startchar]
                left += 1

            #done failing. we pass, comapre now
            temp = right - left + 1
            if temp > maxlength:
                maxlength = temp

            right += 1

        return maxlength
                    




