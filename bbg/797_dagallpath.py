class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1

        #every single path possible
        res = []
        partial = []

        def dfs(cur,target):
            if cur == target:
                res.append(partial[:])
                return
            
            for i in graph[cur]:
                partial.append(i)
                dfs(i, target)
                partial.pop()

        partial.append(0)
        dfs(0, target)
        return res            
            
            

         
            

