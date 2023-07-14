class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        islands = 0


        def dfs(row, col, grid):
            
            dirs = [(1,0), (0,1), (-1,0),(0,-1)]

            grid[row][col] = "0"

            for rdir, cdir in dirs:
                if 0 <= row + rdir < rows and 0 <= col + cdir < cols:
                    if grid[row + rdir][col + cdir] == '1':
                        dfs(row + rdir, col + cdir, grid)
            return


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    #do dfs now on this
                    islands += 1
                    dfs(row, col, grid)

        return islands

        