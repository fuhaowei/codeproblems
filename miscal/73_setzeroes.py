#


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #check whether first rol and col has any 0s. if have, just set a placement that there is, later shift to 0. don't want to set now bcs other places might have zero


        #then iterate rest of the squares. if have 0, set a 0 in the 0th row and col, to flag that that row and col needs to be 0 ed.

        #iterate rest of squares again, check if row and col is 0, if either 0 then we set that square to be 0
        
        #set the last rows as 0 

        #return the matrix

        m = len(matrix)
        n = len(matrix[0])

        zerorow = False
        zerocol = False


        for i in range(m):
            if matrix[i][0] == 0:
                zerorow = True


        for i in range(n):
            if matrix[0][i] == 0:
                zerocol = True

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if zerorow:
            for i in range(m):
                matrix[i][0] = 0

        if zerocol:
            for i in range(n):
                matrix[0][i] = 0


        return matrix
