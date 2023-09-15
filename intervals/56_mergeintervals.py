#maintain a res list, always compare new interval to the last thing
#in res list
#rmbr -> secret is max(xstart,ystart) and min(xend,yend)
#smallest end - biggest start, if it's negative then there's no overlap
#bcs the smallest end is larger than the bigger start 
#distance is also size of overlap



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])


        res = [intervals[0]]
        #[[1,3]]
        for idx in range(1, len(intervals)):
            xstart, xend = intervals[idx][0], intervals[idx][1]
            ystart, yend = res[-1][0], res[-1][1]
            
            overlap = min(xend,yend) - max(xstart,ystart)
            #no overlap
            if overlap < 0:
                res.append(intervals[idx])
            #overlapped!
            else:
                #merge with res
                res.pop()
                res.append([min(xstart,ystart), max(xend,yend)])

        return res

