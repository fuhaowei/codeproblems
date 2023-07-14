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


 ms