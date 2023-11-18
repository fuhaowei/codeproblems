from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        #"abcdef" -> s
        #"ghijkl" -> t

        dicts = Counter(s)
        dictt = Counter(t)

        print(dicts)
        print(dictt)

        #count all differences
        noneed_change = 0
        for letter, count in dictt.items():
            if letter in dicts:
                #why don't i need to change?
                if dictt[letter] > dicts[letter]:
                    noneed_change += dicts[letter]
                else:
                    noneed_change += dictt[letter]

        return len(s)- noneed_change


        #in one step, choose any char of t, replace w another char
        
        