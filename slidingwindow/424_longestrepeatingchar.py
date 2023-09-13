#why are we not shrinking the window? :D
#because we only care for the next biggest size. if something passed alr, i  just update 
#then i expand. if it fails, why would i shrink? i dont care. i just want to check if the next biggest size is avail, so i shift right.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        right = 0
        lens = len(s)

        freqcount = defaultdict(int)
        
        def findmax(thedict):
            return max(thedict.values())

        def cond(thedict):
            if (right - left + 1 - findmax(thedict) <= k):
                return True
            else:
                return False

        longestlength = 0


        #first we need to expand our window until we hit our condition
        while right < lens:

            #process rightmost character
            freqcount[s[right]] += 1

            #cond hit. expand more
            if cond(freqcount):
                longestlength = max(longestlength, right-left +1)
                right += 1
            
            #cond missed.
            else:
                freqcount[s[left]] -= 1
                left += 1
                right += 1
            
        return longestlength




            #if cond is hit, process
            #then shrink the lp by 1
            #then continue shifting/expanding window to the right
             
