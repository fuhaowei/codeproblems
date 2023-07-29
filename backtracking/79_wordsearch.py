#impt takeways: firstly, if u call the backtrack function, rmbr to return if it it's true. u can't just call,
#even if u return in the function itself, u need to return the func call itself too
#secondly, rmbr to keep track of path if thigns say only need once. the other backtrackign stuff
#does that automatically bcs it builds towards a solution 1d right -> only towards the right for subset and 
#combi sum ststuff
#however, this is 4d. it can hit back to the path that u originally were in. hence
#keep track of path in a set!since they say can only use once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not word:
            return False

        m = len(board)
        n = len(board[0])

        possible = []

        #find the starting letter in the board
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    possible.append((row,col))

        if len(possible) == 0:
            return False


        res = []
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]


        def backtrack(row, col, idx, path):

            if idx == len(word):
                return True
            
            for dirx, diry in dirs:
                if 0 <= row + dirx < m and 0 <= col + diry < n:
                    if board[row+dirx][col+diry] == word[idx]:
                        if (row+dirx, col + diry) not in path:
                            path.add((row+dirx,col+diry))
                            if backtrack(row+dirx, col + diry, idx + 1, path):
                                return True
                            else:
                                path.remove((row+dirx, col+diry))

            #went through all directions, don't hv next letter
            return False             


        for row, col in possible:
            #start bfs(backtrack optimized)
            path = set()
            path.add((row,col))
            if backtrack(row, col, 1, path):
                return True
            

        return False


