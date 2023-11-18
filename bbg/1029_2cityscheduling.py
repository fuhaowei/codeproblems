#greedy problem, crux of it is understanding we can sort by the cost of sending to b instead of a, minimizng that

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:


        #can full backtrack
        #can backtrack + cache


        #company wants to interview 2n people

        #costs[i] = [aCosti, bCosti]


        #optimal -> min cost each city

        #but might not be split equally

        #assuming a has more lower cost flights for example.

        #we want to minimize the amount needed to flip people from a to b

        #imagine if everyone cheapest -> A (x)
        #everyone cheapest -> B (y)

        res = []

        for [costa, costb] in costs:
            res.append((costb -costa, costa, costb))

        res.sort()

        #we now have,in order, a list of how much more it would cost to send to b instead of a.
        #so we take half of this (minimize, the rest send to A)
        totalcost = 0

        for i in range(len(costs)//2):
            totalcost += res[i][2]

        for i in range(len(costs)//2,len(costs)):
            totalcost += res[i][1]
            
            
        return totalcost


        