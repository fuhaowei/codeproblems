#key notes -> bfs out layer by layer, try to
#find the optimal BFS in this case.


from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        #if it's 0, just leave it at 0.
        #if i find a 1, then bfs from the coordiantes to find the nearest 0.
        # replace with the distance.


        m = len(mat)
        n = len(mat[0])


        queue = deque()

        #find the 0s
        #replace the 1s


        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    mat[row][col] = "*"
                else:
                    queue.append((row,col))


        #do bfs starting from the 0s. if we visited a non-visited thing, then we
        #append into the end


        dirs = [(1,0), (0,1), (-1,0), (0, -1)]

        while queue:
            #this is a 0 we need to bfs from
            temp = queue.popleft()


            for dir in dirs:
                rdir = dir[0] + temp[0]
                cdir = dir[1] + temp[1]

                if 0 <= rdir < m and 0 <= cdir < n:
                    #first time we meet something, 
                    if mat[rdir][cdir] == "*":
                        mat[rdir][cdir] = mat[temp[0]][temp[1]] + 1
                        #bfs out from this also
                        queue.append((rdir,cdir))

        return mat
                        


            



