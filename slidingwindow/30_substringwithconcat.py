#intimidating but not too tricky, remember Counter, defaultdict to help.
#also the indexing is tricky -> +1, -1, be careful, try writing out? or reasoning out

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        wordlen = len(words[0])
        windowlen = len(words) * wordlen  

        left = 0
        ans = []

        for right in range(windowlen-1 ,len(s)):

            flag = True
            wordcounts = Counter(words)

            currentwindow = s[left:right+1]

            #in a window now, process what's inside
            for i in range(0, windowlen, wordlen): 
                curword = currentwindow[i:i+wordlen]
                if curword in wordcounts:
                    wordcounts[curword] -= 1
                    if wordcounts[curword] < 0:
                        flag = False
                        break
                else:
                    flag = False
                    break

            if flag:
                if all(val == 0 for val in wordcounts.values()):
                    ans.append(left)

            left += 1

        return ans





            

        
        
