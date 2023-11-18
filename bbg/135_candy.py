class Solution:
    def candy(self, ratings: List[int]) -> int:

        candies = [1 for _ in range(len(ratings))]

        for idx in range(len(ratings)):
            #check behind
            if idx == 0:
                continue
            else:
                print(idx)
                if ratings[idx-1] < ratings[idx]:
                    candies[idx] = candies[idx-1] + 1
        
        for idx in range(len(ratings)-1 , -1, -1):
            #check from back
            if idx == len(ratings) -1:
                continue

            else:
                if ratings[idx+1] < ratings[idx]:
                    candies[idx] = max(candies[idx], candies[idx+1]+1)
        

        return sum(candies)


            