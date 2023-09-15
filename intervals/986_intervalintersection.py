#two pointers on the interval lists! cool concept

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        #one way -> merge the 2 sorted lists together o(m + n)
        #basically do merge interval tracking right, compare with previous

        #how about the scan through way?
        fp = 0
        lenf = len(firstList)
        sp = 0
        lens = len(secondList)

        res = []

        while fp < lenf and sp < lens:
            fstart,fend = firstList[fp][0], firstList[fp][1]
            sstart,send = secondList[sp][0], secondList[sp][1]

            #check for overlap:
            maxstart = max(fstart,sstart)
            minend = min(fend, send)

            overlap = minend - maxstart
            
            #if no overlap
            if overlap < 0:
                #move the pointer with the smaller end forward
                if send == minend:
                    sp += 1
                elif fend == minend:
                    fp += 1
            else:
                #overlap, figure out how much overlapped
                res.append([maxstart,maxstart+ (overlap)])
                if send == minend:
                    sp += 1
                elif fend == minend:
                    fp += 1

        #later on nothing else should overlap already


        return res




