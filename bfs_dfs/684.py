#taste of union find
#tricky stuff -> the size of the array at first. other than that not v hard to implement

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges) + 1
        
        par = [-1 for i in range(n)]
        rank = [0] * n


        #joins x and y together, based on ranking
        def union(x,y): 
                xpar = find(x)
                ypar = find(y)

                #this means cycle has been found
                if xpar == ypar:
                    return False
                else:
                    #x is the bigger tree
                    if rank[xpar] > rank[ypar]:
                        #par of y should be x
                        par[ypar] = xpar
                        rank[xpar] += 1
                        return True

                    else:
                        par[xpar] = ypar
                        rank[ypar] += 1
                        return True


        #basically find the parent of x. if the parent of x is x, then we've hit
        #the root node. else, we go up one level recursively
        def find(x):
            if par[x] == -1:
                return x
            par[x] = find(par[x])
            return par[x]

        for x,y in edges:
            if not union(x,y):
                return [x,y]

