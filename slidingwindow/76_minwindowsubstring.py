class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freqtable = {}

        for letter in t:
            if letter in freqtable:
                freqtable[letter] += 1
            else:
                freqtable[letter] = 1
            
        #freq table done, now start windows

        left = 0
        right = 0
        lens = len(s)
        count = len(t)

        smallest = float('inf')
        substring = ""

        def everyvalue(hashmap):
            return all(val <= 0 for val in hashmap.values())

        while right < lens:

            #get new and current char to add to our window
            endchar = s[right]
            if endchar in freqtable:

                if freqtable[endchar] > 0:
                    count -= 1
                freqtable[endchar] -= 1

                #check if I met condition yet
                    #process now.
                while count == 0 and everyvalue(freqtable):
                    if right - left + 1 < smallest:
                        smallest = right - left + 1
                        substring = s[left:right+1]
                    #shrink window
                    startchar = s[left]
                    if startchar in freqtable:
                        freqtable[startchar] += 1
                        if freqtable[startchar] > 0:
                            count += 1
                    left += 1
            
            right += 1

        return substring if smallest != float('inf') else ""
