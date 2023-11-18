
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:


        #n friends, 
        #preferences, at every index i have friend list rankings, 0 to n-1 

        #divided into this list 

        #pairs = [[0,1], [2,3]]


        #friend x is unhappy if x is with y, u is with v, but 
        
        #x unhappy IF BOTH CONDITIONS MET
        # 1) x likes u over y
        # 2) u likes x over v


        #we try to precalculate the happy/unhappy 

        ratherbewith = defaultdict(set)

        # indexes = {}

        unhappy = 0


        #o(n^2)
        for idx in range(len(pairs)):

            paira, pairb = pairs[idx]

            #calculate pair a
            friendrankings = preferences[paira]
            for friend in friendrankings:
                if friend != pairb:
                    ratherbewith[paira].add(friend)
                else:
                    break

            friendrankings2 = preferences[pairb]
            for friend in friendrankings2:
                if friend != paira:
                    ratherbewith[pairb].add(friend)
                else:
                    break

            # indexes[paira] = idx
            # indexes[pairb] = idx
        

        #in every set is the people they wld rather be with - 

        for paira, pairb in pairs:

            #for a, we loop through all the other people w wld rather be paired with
            for otherfriend in ratherbewith[paira]:

                #for each other person, we check if i wld rather be with
                #this dude
                if paira in ratherbewith[otherfriend]:
                    unhappy += 1
                    break

            for otherfriend in ratherbewith[pairb]:

                #for each other person, we check if i wld rather be with
                #this dude
                if pairb in ratherbewith[otherfriend]:
                    unhappy += 1
                    break

        return unhappy






        