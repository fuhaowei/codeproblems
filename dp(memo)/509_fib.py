class Solution:
    def fib(self, n: int) -> int:

        memotable = {}
        
        def recurse(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            if i in memotable:
                return memotable[i]
            else:
                temp = recurse(i-1) + recurse(i-2)
                memotable[i] = temp
                return temp

        return recurse(n)