class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)

        adjlist = {i:[] for i in range(n)}


        for city1 in range(n):
            for city2 in range(n):

                if isConnected[city1][city2] == 1:
                    adjlist[city1].append(city2)
                    adjlist[city2].append(city1)


        visited = set()
        province = 0

        def dfs(cities):
            if cities:
                for city in cities:
                    if city not in visited:
                        visited.add(city)
                        dfs(adjlist[city])


        for city in range(n):
            if city not in visited:
                province += 1
                print(adjlist[city])
                dfs(adjlist[city])

        return province



#also union find approach. fk it lol just dfs for this.
# par and rank are 1-indexed, but you use them as if they were 0-indexed. This will cause an IndexError.
# In your union function, you're updating the parents of x and y directly, instead of their root parents (parx and pary).
# In the final count, you're counting -1 values as separate sets, which is incorrect.


# he parent and rank arrays are 0-indexed to match the 0-indexed isConnected matrix.
# The union function updates the parents of parx and pary, not x and y.
# The find function implements path compression by setting par[x] to find(par[x]), which makes subsequent find operations on the same element faster.
# In the loop that calls union, the column starts from row, because the isConnected matrix is symmetric (i.e., if city i is connected to city j, then city j is connected to city i).
# The final count uses a list comprehension to count the number of root nodes (i.e., nodes whose parent is -1), which gives the number of provinces.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        #use union find to find the total number of unconnected provinces

        n = len(isConnected)

        par = [-1] * (n)
        rank = [0] * (n)

        def find(x):
            #haven't initialized it yet
            if par[x] == -1:
                return x
                #this the other optimization, don't forget
            par[x] = find(par[x])
            return par[x]


        def union(x,y):

            xpar = find(x)
            ypar = find(y)
            # # #this means that they are back to the same node! cycle!
            if xpar == ypar:
                return

            if rank[xpar] > rank[ypar]:
                par[ypar] = xpar
                rank[x] += 1

            elif rank[xpar] < rank[ypar]:
                par[xpar] = ypar
                rank[y] += 1

            else:
                par[xpar] = ypar
    


        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    union(row, col)


        #count unique numbers in par

        return sum([par[i] == -1 for i in range(n)])
                
                

        