
#Exactly! This algorithm is essentially letting each number take its turn at being placed at the end of the permutation, while it recursively generates permutations of the remaining numbers. This systematic way of exploring all possibilities ensures that all permutations are generated.

# And you're correct in your understanding that despite this structure, due to the recursive nature of the implementation, each number will still end up in all possible positions across different permutations. This is one of the fascinating aspects of recursive solutions - it may look like we're always appending the element at the end, but due to the nature of recursion, it ends up being in different positions in the final set of permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []


        #base case -> if only one possible permutation
        #return a list contaiing nums as only element
        #need to deep copy else we get a reference to list
        #rmbr passing lsit to funciton in python is by reference, not copy

        if len(nums) == 1:
            return [nums[:]]

        #base case

        for i in range(len(nums)):
            #slowly from the start pop off each element from the front
            #u realize that by popping off, you're saying that 
            #hey, let's start this permutation from this end now
            n = nums.pop(0)

            #go and iterate with the rest
            perms = self.permute(nums)


            #with the rest of the possible permutations, append n to the end
            for perm in perms:
                perm.append(n)

            #add to result
            res.extend(perms)

            #finally, clean up! for other permutations our n must be possible. add to back
            nums.append(n)

        return res

