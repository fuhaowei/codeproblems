from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m = len(rooms)
        n = len(rooms[0])

        gates = []

        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    gates.append((row,col))


        #now we have this row and col tuple, we need to figure out a way
        #to bfs from them

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque(gates)

        while queue:

            (row, col) = queue.popleft()

            #update neighbors + put them on queue
            for dirx,diry in dirs:
                newx = dirx + row
                newy = diry + col

                if 0 <= newx < m and 0 <= newy < n:
                    if rooms[newx][newy] != -1 or rooms[newx][newy] != 0:
                        if rooms[newx][newy] > rooms[row][col]:
                            rooms[newx][newy] = rooms[row][col] + 1
                            queue.append((newx,newy))
                




        